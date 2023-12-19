# middleware.py
from django.http import HttpResponseForbidden

class MaxConnectionsMiddleware:
    MAX_CONNECTIONS = 5
    connection_count = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        remote_ip = request.META.get('REMOTE_ADDR')

        if remote_ip not in self.connection_count:
            self.connection_count[remote_ip] = 1
        else:
            self.connection_count[remote_ip] += 1

        if self.connection_count[remote_ip] > self.MAX_CONNECTIONS:
            return HttpResponseForbidden("Too many requests from your IP address.")

        response = self.get_response(request)
        return response
