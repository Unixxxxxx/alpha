# about/middleware.py

from django.http import HttpResponseForbidden

class BlockBadUrlsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_paths = ['/hack/', '/test/', '/admin123/']

        if request.path in blocked_paths:
            return HttpResponseForbidden("Blocked URL")

        return self.get_response(request)
