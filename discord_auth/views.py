"""Views for handling discord authorisation."""
import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect

REDIRECT_URI = 'https://discordapp.com/api/oauth2/authorize?client_id=644830838462218241&redirect_uri=https%3A%2F%2Fhacksoc-film-night.herokuapp.com%2Fverify&response_type=code&scope=identify'

API_ENDPOINT = 'https://discordapp.com/api/v6'
CLIENT_ID = '644830838462218241'
CLIENT_SECRET = 'rIdG5AnCCWu-eap5-Myasd7BFnXHr6L9'
REDIRECT_URI = 'https://hacksoc-film-night.herokuapp.com/verify'


def auth(request):
    return HttpResponseRedirect(REDIRECT_URI)


def verify(request):
    code = request.GET.get('code', None)


    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify email connections'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()

    print(r.json())


