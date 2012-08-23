# -*- encoding: utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm
from ..utils import get_user


class UserAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            get_user(username, password)
        return super(UserAuthenticationForm, self).clean()
