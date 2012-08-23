# -*- encoding: utf-8 -*-

from django.contrib.auth import login
from django.http import HttpResponseForbidden
from ..utils import get_user, get_partner


class RequestLogin():
    """
    Logins user from partner's domain or
    raises 403 Forbidden error
    """

    def process_view(self, request, *args, **kwargs):
        partner = get_partner(request)
        if partner:
            request.partner = partner
            data = request.GET
            username = data.get('name')

            if username:
                user = get_user(username)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
            elif data.get('error'):
                return HttpResponseForbidden(data.get('error'))
