from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, BooleanField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired

from app.headphones.models import Headphone

class AddHeadphoneForm(FlaskForm):
    brand_id = SelectField('Brand', validators=[DataRequired()])
    type_id = SelectField('Type', validators=[DataRequired()])
    color_id = SelectField('Color', validators=[DataRequired()])
    image_id = SelectField('Image', validators=[DataRequired()])
    model_name = StringField('Model', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    lifetime = IntegerField('Life time', validators=[DataRequired()])
    max_power = IntegerField('Max power', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    impedance = IntegerField('Impedance', validators=[DataRequired()])
    sensitivity = IntegerField('Sensitivity', validators=[DataRequired()])
    lifetime_case = IntegerField('Case life time', validators=[DataRequired()])
    is_nc = BooleanField('Yes')
    is_deleted = BooleanField('Yes')
    submit = SubmitField('Add!')

    def validate_model_name(self, model_name):
        name_headphone = Headphone.query.filter_by(model_name=model_name.data).first()
        if name_headphone is not None:
            raise ValidationError('This model is already in the database.')
            