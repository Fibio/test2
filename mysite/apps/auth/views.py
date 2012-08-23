# -*- encoding: utf-8 -*-

from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserAuthenticationForm
from ..utils import get_partner


def auth_login(request):
    partner = get_partner(request)
    form = UserAuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'auth/login.html', {'form': form, 'partner': partner})


def partner_login(request):
    """ Emulates partner login system
    """
    if request.method == "GET":
        data = request.GET
        username = data.get('username')
        if username == 'Vasya':
            redirect_to = '{}?name={}'.format(data.get('next'), username)
        else:
            message = "User {} doesn't exist".format(username)
            redirect_to = '{}?error={}'.format(data.get('next'), message)

        return HttpResponseRedirect(redirect_to)
