from flask import abort, Blueprint, render_template, flash, redirect, url_for

from app.db import db
from app.users.decorators import admin_required
from app.headphones.models import Brand, HeadphoneType, Color, AddImage, Headphone
from app.headphones.forms import AddHeadphoneForm
from app.headphones.models import Headphone

blueprint = Blueprint('headphone', __name__, url_prefix='/')

@blueprint.route('/headphones/<int:headphones_id>')
def catalog_headphone(headphone_id):
    hp = Headphone.query.filter(Headphone.id == headphone_id).first()

    if not hp:
        abort(404)

    return render_template('index.html', page_title=hp.title, headphones=hp)

@blueprint.route('/add_hp', methods=['GET', 'POST'])
@admin_required
def add_headphones():
    form = AddHeadphoneForm()
    if form.validate_on_submit():
        headphones = Headphone(
                    brand_id=form.brand.data,
                    type_id=form.type.data,
                    color_id=form.color.data,
                    image_id=form.image.data,
                    model_name=form.model.data,
                    price=form.price_cost.data,
                    lifetime=form.life_time.data,
                    max_power=form.maxpower.data,
                    weight=form.weight_numeric.data,
                    impedance=form.impedance_numeric.data,
                    sensitivity=form.sensitivity_numeric.data,
                    lifetime_case=form.lifetime_case_numeric.data,
                    is_nc=form.is_nc_bool.data,
                    is_deleted=form.is_deleted_bool.data)                    
        db.session.add(headphones)
        db.session.commit()
        flash('Success! This headphone has been added!')
        return redirect(url_for('headphone.add_headphones'))
    return render_template('add_hp.html', title='Add headphones', form=form)

def save_tables():
    db.session.add(Brand)
    db.session.add(HeadphoneType)
    db.session.add(Color)
    db.session.add(AddImage)
    db.session.add(Headphone)
    db.session.commit()