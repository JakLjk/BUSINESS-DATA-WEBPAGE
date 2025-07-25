import logging
import time

log = logging.getLogger("log_main")

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration_ms = round((time.time() - start_time) * 1000)
        user = getattr(request, "user", None)
        user_str = str(user) if user and user.is_authenticated else "anonymous"

        log.info(
            "Request handled",
            extra={
                "method": request.method,
                "path": request.get_full_path(),
                "status": response.status_code,
                "duration_ms": duration_ms,
                "user": user_str,
                "ip": get_client_ip(request),
            }
        )

        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")