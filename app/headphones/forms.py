from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired


class AddHeadphoneForm(FlaskForm):
    brand_id = SelectField('Brand', coerce=int, Validator=[DataRequired()])
    type_id = SelectField('Type', coerce=int, Validator=[DataRequired()])
    color_id = SelectField('Color', coerce=int, Validator=[DataRequired()])
    image_id = SelectField('Image', coerce=int, Validator=[DataRequired()])
    model_name = StringField('Model', Validator=[DataRequired()])
    price = IntegerField('Price', Validator=[DataRequired()])
    lifetime = IntegerField('Life time', Validator=[DataRequired()])
    max_power = IntegerField('Max power', Validator=[DataRequired()])
    weight = IntegerField('Weight', Validator=[DataRequired()])
    impedance = IntegerField('Impedance', Validator=[DataRequired()])
    sensitivity = IntegerField('Sensitivity', Validator=[DataRequired()])
    lifetime_case = IntegerField('Case life time', Validator=[DataRequired()])
    is_nc = BooleanField('Yes')
    is_deleted = BooleanField('Yes')
            