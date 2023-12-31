from datetime import datetime
from flask_smorest import abort, Blueprint
from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from schemas import FactoryUpdateSchema
from models import SprocketModel
from schemas import SprocketSchema
from schemas import PlainSprocketSchema
from schemas import ChartDataSchema, PlainChartDataSchema
from models.chart_data import ChartDataModel
from models.factory import FactoryModel
from schemas import FactorySchema
from db import db

factoryBlueprint = Blueprint(
    'factory', 'factory', url_prefix='/factory',
    description='Operations on factories'
)

@factoryBlueprint.route('/')
class FactoryView(MethodView):
    @factoryBlueprint.response(200, FactorySchema(many=True))
    def get(self):
        return FactoryModel.query.all()

@factoryBlueprint.route('/<int:factory_id>')
class FactoryView(MethodView):

    @factoryBlueprint.arguments(FactorySchema)
    @factoryBlueprint.response(201, FactorySchema)
    def post(self, factory_data, factory_id):
        factory = FactoryModel(id=factory_id, **factory_data)
        try:
            db.session.add(factory)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return factory, 201
    
    @factoryBlueprint.response(200, FactorySchema)
    def get(self, factory_id):
        factory = FactoryModel.query.get_or_404(factory_id)
        if factory is None:
            abort(404, message="Factory not found")
        return factory

    @factoryBlueprint.arguments(FactoryUpdateSchema)
    @factoryBlueprint.response(200, FactoryUpdateSchema)
    def put(self, factory_data, factory_id):
        factory = FactoryModel.query.get_or_404(factory_id)
        if factory is None:
            abort(404, message="Factory not found")
        factory.name = factory_data['name']
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return factory

    @factoryBlueprint.response(204)
    def delete(self, factory_id):
        factory = FactoryModel.query.get_or_404(factory_id)
        if factory is None:
            abort(404, message="Factory not found")
        try:
            db.session.delete(factory)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return {}, 204
    
@factoryBlueprint.route('/<int:factory_id>/chart/<chart_id>')
class FactoryView(MethodView):
    @factoryBlueprint.arguments(PlainChartDataSchema)
    @factoryBlueprint.response(200, FactorySchema)
    def put(self, chart_data, factory_id, chart_id):
        factory = FactoryModel.query.get_or_404(factory_id)
        if factory is None:
            abort(404, message="Factory not found")
        chart = ChartDataModel.query.get(chart_id)
        if chart is None:
            chart = ChartDataModel(id=chart_id, **chart_data)
        else:
            abort(400, message="Chart already exists")
        factory.chart_data.append(chart)
        try:
            db.session.add(chart)
            db.session.add(factory)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return factory
    

@factoryBlueprint.route('/<int:factory_id>/sprocket/<int:sprocket_id>')
class FactoryView(MethodView):
    @factoryBlueprint.arguments(PlainSprocketSchema)
    @factoryBlueprint.response(200, FactorySchema)
    def put(self, sprocket_data, factory_id, sprocket_id):
        factory = FactoryModel.query.get_or_404(factory_id)
        if factory is None:
            abort(404, message="Factory not found")
        sprocket = SprocketModel.query.get(sprocket_id)
        if sprocket is None:
            sprocket = SprocketModel(id = sprocket_id, **sprocket_data, factory_id = factory_id)
        factory.sprockets.append(sprocket)
        try:
            db.session.add(sprocket)
            db.session.add(factory)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Internal server error")
        return factory