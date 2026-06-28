from django.http import HttpResponseForbidden


class AdminIPWhitelistMiddleware:
    ALLOWED_IPS = [
        "127.0.0.1",
        "::1",
        "49.205.207.136",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        if request.path.startswith("/admin/"):
            if ip not in self.ALLOWED_IPS:
                return HttpResponseForbidden("Access Denied")

        return self.get_response(request)
