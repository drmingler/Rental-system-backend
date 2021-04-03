from rest_framework.exceptions import APIException


class UploadLimitReached(APIException):
    status_code = 403
    default_detail = (
        "Free property upload limit reached, please subscribe to upload more properties"
    )


class InvalidPayloadReached(APIException):
    status_code = 400
    default_detail = f"Invalid property upload payload"
