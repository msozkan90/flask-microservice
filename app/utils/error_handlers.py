from flask import Blueprint
from marshmallow import ValidationError
from app.utils.response import error_response

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(ValidationError)
def handle_validation_error(err):
    return error_response(str(err), 422)

@error_bp.app_errorhandler(404)
def handle_404(err):
    return error_response("Resource not found", 404)

@error_bp.app_errorhandler(Exception)
def handle_exception(err):
    return error_response(str(err), 500)
