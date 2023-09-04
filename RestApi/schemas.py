from marshmallow import Schema, fields, validate

class PlainChartDataSchema(Schema):
    #The base information of a Char_Data based on the Json file received
    sprocket_production_goal = fields.Int()
    sprocket_production_rate = fields.Int()
    time = fields.Int()

class PlainFactorySchema(Schema):
    #The factory had to have an ID to be able to search for it in the GET endpoint
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(min=1, max=50))

class PlainSprocketSchema(Schema):
    #The base information of a sprocket based on the Json file received
    id = fields.Int(dump_only=True)
    teeth = fields.Int()
    pitch_diameter = fields.Int()
    outside_diameter = fields.Int()
    pitch = fields.Int()

class SprocketSchema(PlainSprocketSchema):
    #This is a custom thing I made to be able to define which factory is producing which sprocket
    factory_id = fields.Int(load_only=True, nullable=True)
    factory = fields.Nested(PlainFactorySchema(), dump_only=True, load_only=True, nullable=True)

class ChartDataSchema(PlainChartDataSchema):
    #The chart data is related to the factory
    factory_id = fields.Int(dump_only=True, load_only=True)
    factory = fields.Nested(PlainFactorySchema(), dump_only=True, load_only=True)

class FactorySchema(PlainFactorySchema):
    #This add the value of the sprockets and the chart data schemas I defined before this to the factory
    sprockets = fields.List(fields.Nested(SprocketSchema(), dump_only=True, default=[]))
    chart_data = fields.List(fields.Nested(ChartDataSchema(), dump_only=True, default=[]))

class FactorySprocketSchema(Schema):
    #This is a custom thing I made, but in this case is defined since the relationship between factories and sprockets is many-to-many
    factory = fields.Nested(PlainFactorySchema())
    sprocket = fields.Nested(PlainSprocketSchema())

class FactoryUpdateSchema(Schema):
    #The only value that can be updated to a factory on its own is the name
    name = fields.Str(validate=validate.Length(min=1, max=50), required=False)
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