from django.shortcuts import render_to_response
from django.template.context import RequestContext

from allauth.account.views import LogoutView


class My_LogoutView(LogoutView):
    return render_to_response(
	'home.html',
	{ 'user': request.user }
	)
