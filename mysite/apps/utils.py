# -*- encoding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings


def get_user(username, password='', commit=True):
    """ Gets user or creates him with password
    """
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = User(username=username)
        user.set_password(password)
        user.save(commit)
    return user


def get_partner(request):
    partner = False
    next = request.GET.get('next', '') or request.META.get('HTTP_REFERER', '')
    if next:
        for domain in settings.PARTNERS_DOMAINS:
            if domain in next:
                partner = next
                break
    return partner
