import math
from gettext import ngettext

from django.http import JsonResponse
from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import APIException



# Como lançar uma exception
# from product.api.exceptions import ProductOutOfStock

# raise ProductOutOfStock(detail='Fora De Estoque',code='200')



# Exceção customizada


class ProductOutOfStock(APIException):
    status_code = status.HTTP_200_OK
    default_detail = ('Produto Indisponível.')
    default_code = 'produto sem estoque'



# EXCEÇOES PADRAO

class ParseError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('Malformed request.')
    default_code = 'parse_error'


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = ('Incorrect authentication credentials.')
    default_code = 'authentication_failed'


class NotAuthenticated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = ('Authentication credentials were not provided.')
    default_code = 'not_authenticated'


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ('You do not have permission to perform this action.')
    default_code = 'permission_denied'


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ('Not found.')
    default_code = 'not_found'


class MethodNotAllowed(APIException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = ('Method "{method}" not allowed.')
    default_code = 'method_not_allowed'

    def __init__(self, method, detail=None, code=None):
        if detail is None:
            detail = force_str(self.default_detail).format(method=method)
        super().__init__(detail, code)


class NotAcceptable(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = ('Could not satisfy the request Accept header.')
    default_code = 'not_acceptable'

    def __init__(self, detail=None, code=None, available_renderers=None):
        self.available_renderers = available_renderers
        super().__init__(detail, code)


class UnsupportedMediaType(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    default_detail = ('Unsupported media type "{media_type}" in request.')
    default_code = 'unsupported_media_type'

    def __init__(self, media_type, detail=None, code=None):
        if detail is None:
            detail = force_str(self.default_detail).format(media_type=media_type)
        super().__init__(detail, code)


class Throttled(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = ('Request was throttled.')
    extra_detail_singular = ('Expected available in {wait} second.')
    extra_detail_plural = ('Expected available in {wait} seconds.')
    default_code = 'throttled'

    def __init__(self, wait=None, detail=None, code=None):
        if detail is None:
            detail = force_str(self.default_detail)
        if wait is not None:
            wait = math.ceil(wait)
            detail = ' '.join((
                detail,
                force_str(ngettext(self.extra_detail_singular.format(wait=wait),
                                   self.extra_detail_plural.format(wait=wait),
                                   wait))))
        self.wait = wait
        super().__init__(detail, code)


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'Server Error (500)'
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def bad_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    data = {
        'error': 'Bad Request (400)'
    }
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)