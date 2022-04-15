from flask import Blueprint, render_template

from app.headphones.models import Headphone

blueprint = Blueprint('main', __name__, url_prefix='/')

"""
@blueprint.route('/index')
def index_page():
    text = {'text': 'Test'}
    items = [
        {
            'brand': {'text': 'Catalog'},
            'body': 'Wireless headphones'
        }
    ]
    return render_template('index.html', title='Home Page', items=items)
"""

def get_catalog_headphones():
    headphones = Headphone.query.order_by(Headphone.model_name).all()
    return headphones


@blueprint.route('/index')
def index_page():
    headphones = get_catalog_headphones()
    title = "Wireless headphones"
    return render_template('index.html', page_title=title, headphones=headphones)