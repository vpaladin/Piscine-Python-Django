from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request:HttpRequest):
        response = self.get_response(request)
        return response

    def process_template_response(self, request: HttpRequest, response: HttpResponse):
        response.context_data['login_form'] = AuthenticationForm
        return response