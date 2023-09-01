from datetime import datetime
from flask_smorest import abort, Blueprint
from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from schemas import PlainSprocketSchema
from schemas import SprocketSchema
from models import FactoryModel, SprocketModel
from schemas import FactorySchema
from db import db

sprocketBlueprint = Blueprint(
    'sprocket', 'sprocket', url_prefix='/sprocket',
    description='Operations on sprockets'
)

@sprocketBlueprint.route('/')
class SprocketView(MethodView):
    @sprocketBlueprint.response(200, SprocketSchema(many=True))
    def get(self):
        return SprocketModel.query.all()
    
@sprocketBlueprint.route('/<int:sprocket_id>')
class SprocketView(MethodView):
    @sprocketBlueprint.arguments(SprocketSchema)
    @sprocketBlueprint.response(201, SprocketSchema)
    def post(self, sprocket_data, sprocket_id):
        sprocket = SprocketModel(id = sprocket_id, **sprocket_data)
        try:
            db.session.add(sprocket)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return sprocket, 201
    
    @sprocketBlueprint.response(200, SprocketSchema)
    def get(self, sprocket_id):
        sprocket = SprocketModel.query.get_or_404(sprocket_id)
        if sprocket is None:
            abort(404, message="Sprocket not found")
        return sprocket
    
    @sprocketBlueprint.arguments(PlainSprocketSchema)
    @sprocketBlueprint.response(200, PlainSprocketSchema)
    def put(self, sprocket_data, sprocket_id):
        sprocket = SprocketModel.query.get_or_404(sprocket_id)
        if sprocket is None:
            abort(404, message="Sprocket not found")
        
        sprocket.teeth = sprocket_data['teeth']
        sprocket.pitch_diameter = sprocket_data['pitch_diameter']
        sprocket.outside_diameter = sprocket_data['outside_diameter']
        sprocket.pitch = sprocket_data['pitch']
        try:
            db.session.add(sprocket)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return sprocket
    
    @sprocketBlueprint.response(204)
    def delete(self, sprocket_id):
        sprocket = SprocketModel.query.get_or_404(sprocket_id)
        if sprocket is None:
            abort(404, message="Sprocket not found")
        try:
            db.session.delete(sprocket)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return None
