from marshmallow import Schema, fields, validate

class PlainChartDataSchema(Schema):
    sprocket_production_goal = fields.Int()
    sprocket_production_rate = fields.Int()
    time = fields.Int()

class PlainFactorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(min=1, max=50))

class PlainSprocketSchema(Schema):
    id = fields.Int(dump_only=True)
    teeth = fields.Int()
    pitch_diameter = fields.Int()
    outside_diameter = fields.Int()
    pitch = fields.Int()

class SprocketSchema(PlainSprocketSchema):
    factory_id = fields.Int(load_only=True)
    factory = fields.Nested(PlainFactorySchema(), dump_only=True, load_only=True)

class ChartDataSchema(PlainChartDataSchema):
    factory_id = fields.Int(dump_only=True, load_only=True)
    factory = fields.Nested(PlainFactorySchema(), dump_only=True, load_only=True)

class FactorySchema(PlainFactorySchema):
    #sprockets only works for knowning which sprockets are being produced in the factory
    sprockets = fields.List(fields.Nested(SprocketSchema(), dump_only=True, default=[]))
    chart_data = fields.List(fields.Nested(ChartDataSchema(), dump_only=True, default=[]))
'''
I would have added an order schema and a stock control for the sprockets so it would be something like this

class OrderSchema(Schema):
    factory_id = fields.Int()
    factory = fields.Nested(FactorySchema(), dump_only=True)
    item_list = fields.List(fields.Nested(PlainSprocketSchema(), dump_only=True))
    quantity = fields.List(fields.Int(), dump_only=True)
    date = fields.DateTime()

class StockControlSchema(Schema):
    factory_id = fields.Int()
    factory = fields.Nested(FactorySchema(), dump_only=True)
    sprocket = fields.Nested(PlainSprocketSchema(), dump_only=True)
    quantity = fields.Int()
    date = fields.DateTime()

class FactorySchema(PlainFactorySchema):
    orders = fields.List(fields.Nested(OrderSchema(), dump_only=True))
    stock_control = fields.List(fields.Nested(StockControlSchema(), dump_only=True))

    
So when an order is taken, the value will be related to the Stock
and the stock will be related to the factory

So once a user buys an sprocket order, that can be many the sprocket count will be reduced from the stock
and the stock will be reduced from the factory

with this we can keep a more accurate count of the sprockets and the stock and the production related to it

if you have too much stock you are producing too many sprockets of the same value and they are not being sold

if you are always short on stock then it means that the production is not enough to cover the orders

so it would be a more accurate way to keep track of the production and the orders
'''