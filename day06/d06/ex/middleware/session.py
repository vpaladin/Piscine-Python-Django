from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time
import random

# текущее время 16 часов + 3  18 часов
SESSION_TIME = 42
SESSION_TIMEOUT = "Time age"


class AnonymousSessionMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.user.is_authenticated:
            return
        init_time = request.session.setdefault(SESSION_TIMEOUT, time.time())
        if init_time + SESSION_TIME <= time.time():
            request.session.flush()
        request.session.setdefault('anonymous', random.choice(
            settings.USERNAMES))
        request.user.username = request.session.get('anonymous')
