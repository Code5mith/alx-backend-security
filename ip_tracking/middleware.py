from .models import RequestLog
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get client IP
        ip_address = request.META.get('REMOTE_ADDR', '')
        # Log request details
        RequestLog.objects.create(
            ip_address=ip_address,
            path=request.path,
        )
        return self.get_response(request)
