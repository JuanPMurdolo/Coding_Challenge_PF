from db import db

class ChartDataModel(db.Model):
    __tablename__ = "chart_data"

    id = db.Column(db.Integer(), primary_key=True)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.id'), nullable=False)
    factory = db.relationship('FactoryModel', back_populates='chart_data')
    sprocket_production_goal = db.Column(db.Integer(), nullable=False)
    sprocket_production_rate = db.Column(db.Integer(), nullable=False)
    time = db.Column(db.Integer(), nullable=False)