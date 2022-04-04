from app.db import db

class Brand(db.Model):
    __tablename__ = 'brands'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    headphones = db.relationship('Headphone', backref='brand', lazy='dynamic')

    def __repr__(self):
        return '<Brand {}>'.format(self.name)

class HeadphoneType(db.Model):
    __tablename__ = 'headphones_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    headphones = db.relationship('Headphone', backref='type', lazy='dynamic')
    
    def __repr__(self):
        return '<HeadphoneType {}>'.format(self.name)

class Color(db.Model):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    headphones = db.relationship('Headphone', backref='color', lazy='dynamic')

    def __repr__(self):
        return '<Color {}>'.format(self.name)


class AddImage(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    headphones = db.relationship('Headphone', backref='image', lazy='dynamic')

    def __repr__(self):
        return '<Image {}>'.format(self.name)


class Headphone(db.Model):
    __tablename__ = 'headphones'
    
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    model_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)
    lifetime = db.Column(db.Integer)
    max_power = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    impedance = db.Column(db.Integer)
    sensitivity = db.Column(db.Integer)
    lifetime_case = db.Column(db.Integer)
    is_nc = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)

    def __repr__(self):
        return '<Headphone {}>'.format(self.model_name)


