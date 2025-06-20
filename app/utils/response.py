def success_response(data=None, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }, 200

def error_response(message="An error occurred", status_code=400):
    return {
        "status": "error",
        "message": message
    }, status_code
