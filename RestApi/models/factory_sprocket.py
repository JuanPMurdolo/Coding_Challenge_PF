from db import db

class FactorySprocket(db.Model):
    __tablename__ = "factory_sprockets"

    id = db.Column(db.Integer(), primary_key=True)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.id'))
    sprocket_id = db.Column(db.Integer, db.ForeignKey('sprockets.id'))