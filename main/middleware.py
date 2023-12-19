
from .models import RateLimit
from datetime import datetime, timedelta
from django.core.exceptions import PermissionDenied
class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        allowed_requests = 10
        time_window = 60
        rate_limit, created = RateLimit.objects.get_or_create(ip_address=ip_address)
        if (datetime.utcnow() - rate_limit.timestamp).total_seconds() >= time_window:
            rate_limit.connection_number = 0
            rate_limit.save()

        if rate_limit.connection_number >= allowed_requests:
            return PermissionDenied('Too many requests')
        rate_limit.connection_number += 1
        rate_limit.save()

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
