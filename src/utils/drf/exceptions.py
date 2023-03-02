from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def server_error(request, *args, **kwargs):
    """
    通用 500 错误
    """
    data = {"detail": "服务端发生了一点小意外，请稍后再尝试访问。"}
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def not_found(request, *args, **kwargs):
    """
    通用 404 错误
    """
    data = {"detail": "您访问的接口不存在。"}
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def custom_exception_handler(exc, context):
    """自定义错误处理

    Args:
        exc (_type_): _description_
        context (_type_): 上下文

    Returns:
        _type_: _description_
    """
    response = exception_handler(exc, context)

    return response


class GenericValidationError(APIException):
    status_code = 400
    default_detail = "参数不正确，请修改后重试！"
    default_code = "bad_request"
