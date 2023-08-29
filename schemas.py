from marshmallow import Schema, fields, validate

class FactorySchema(Schema):
    id = fields.Str(dump_only=True)
    chart_data = fields.List(fields.List(fields.Int()))
    chart_labels = fields.List(fields.Str())

class SprocketSchema(Schema):
    id = fields.Str(dump_only=True)
    teeth = fields.Int()
    pitch_diameter = fields.Int()
    outside_diameter = fields.Int()
    pitch = fields.Int()

