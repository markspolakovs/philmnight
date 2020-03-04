from django.shortcuts import render
from django.contrib.auth import logout

from django.conf import settings

def index(request):
    return render(request, 'index.html', {'GOOGLE_OAUTH_KEY': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY})


def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})
