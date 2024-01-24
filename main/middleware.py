from datetime import datetime, timezone

from django.conf import settings
from django.db import transaction
from django.http import HttpResponseForbidden, HttpResponse

from .models import RateLimit


class CountryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.COUNTRY_CODE == "RU":
            return HttpResponseForbidden()

        response = self.get_response(request)
        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_static_request = 'static' in request.path
        if not is_static_request and request.path.endswith('/'):
            ip_address = get_client_ip(request)
            allowed_requests = 40
            time_window = 60

            with transaction.atomic():
                rate_limit, created = RateLimit.objects.select_for_update().get_or_create(ip_address=ip_address)
                current_time = datetime.now()

                if (current_time - rate_limit.timestamp).total_seconds() >= time_window:
                    rate_limit.connection_number = 0
                    rate_limit.timestamp = current_time
                    rate_limit.save()

                if rate_limit.connection_number >= allowed_requests:
                    return HttpResponse(status=429)

                rate_limit.connection_number += 1
                rate_limit.save()

        response = self.get_response(request)
        return response
