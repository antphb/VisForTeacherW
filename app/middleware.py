from django.shortcuts import redirect
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not request.path.startswith('/login/') and not request.path.startswith('/password-reset/') and not request.path.startswith('/password-reset/done/') and not request.path.startswith('/admin/') and not request.path.startswith('/password-reset-confirm/') and not request.path.startswith('/password-reset-complete/') and not request.path.startswith('/staticfiles/'):
                return redirect('/login/')

        response = self.get_response(request)
        return response
