from db import db

class FactoryModel(db.Model):
    __tablename__ = "factories"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    chart_data = db.relationship('ChartDataModel', back_populates='factory', lazy='dynamic', cascade="all, delete")
    sprockets = db.relationship('SprocketModel', back_populates='factory', lazy='dynamic', cascade="all, delete")