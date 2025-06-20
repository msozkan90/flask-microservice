from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validates, ValidationError
from app.models.user import User
from app.extensions import db

class UserCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

    email = fields.Email(required=True)
    name = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters.")


class UserResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        exclude = ("password",)
        
    id = fields.Int(dump_only=True)
    email = fields.Email()
    name = fields.Str()