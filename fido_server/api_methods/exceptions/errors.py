from rest_framework.exceptions import APIException


class ProcessNotFinished(APIException):
    status_code = 400
    default_detail = {
        "status": "failure",
        "detail": "OTP generation failure. Please try again!",
    }
