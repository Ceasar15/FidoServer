from rest_framework.exceptions import APIException


class ProcessNotFinished(APIException):
    status_code = 503
    default_detail = {
        "status": "failure",
        "detail": "OTP generation failure. Please try again!",
    }

class WrongPhoneNumber(APIException):
    status_code = 400
    default_detail = {
        "status": "failure",
        "detail": "Pass a valid phone_number",
    }

class UserDataNotFound(APIException):
    status_code = 400
    default_detail = {
        "status": "failure",
        "detail": "Invalid phone number / OTP",
    }
