from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

class AdminBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # check is user try to visit the backstage
        if request.path.startswith('/page-not-found-404/'):
            # if user are not an authenticated user(Anonymous User)
            if not request.user.is_authenticated:
                return HttpResponse("401 Unauthorized: Access is denied.", status=401)
            # if user are not authorized to access
            if not request.user.is_staff:
                raise PermissionDenied 

        return self.get_response(request)