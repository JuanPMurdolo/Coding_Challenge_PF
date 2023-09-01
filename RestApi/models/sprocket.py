from db import db

class SprocketModel(db.Model):
    __tablename__ = "sprockets"

    id = db.Column(db.Integer(), primary_key=True)
    teeth = db.Column(db.Integer(), nullable=False)
    pitch_diameter = db.Column(db.Integer(), nullable=False)
    outside_diameter = db.Column(db.Integer(), nullable=False)
    pitch = db.Column(db.Integer(), nullable=False)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.id'), nullable=False)
    factory = db.relationship('FactoryModel', secondary="factory_sprockets", back_populates='sprockets', lazy='dynamic')  