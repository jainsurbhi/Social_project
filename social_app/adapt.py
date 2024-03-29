from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url
from datetime import datetime, timedelta

class AccountAdapter(DefaultAccountAdapter):

def get_login_redirect_url(self, request):
  

    assert request.user.is_authenticated()
    if not request.user.password:
        url = '/accounts/password/set'
    else:
        url = settings.LOGIN_REDIRECT_URL
    return resolve_url(url)
