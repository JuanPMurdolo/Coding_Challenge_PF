from datetime import datetime
from flask_smorest import abort, Blueprint
from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from RestApi.schemas import SprocketSchema
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
        sprocket = SprocketModel(sprocket_id, **sprocket_data)
        try:
            db.session.add(sprocket)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return sprocket, 201
