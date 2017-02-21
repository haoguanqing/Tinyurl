from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from .models import UrlModel

def encode(request):
    print 'encoding...'
    # get long url from request.POST
    if request.method != 'POST':
        return HttpResponse("Hello, world. You're at the urls index.")
    
    long_url = request.POST.get('long_url', '')
    print(long_url)
    # convert to short url
    newId = UrlModel.objects.latest('id')[0].id + 1;
    short_url = to_base_62(newId)
    # create an object in database
    url = UrlModel.objects.create(
        short_url = short_url,
        long_url = long_url)
    url.save()
    
    return HttpResponse(shortUrl)

def decode(request, short_url):
    # get long url from db
    urlSet = UrlModel.objects.filter(short_url = short_url)
    if len(urlSet) != 1:
        # if does not exist, return error info
        return HttpResponse("url not found")
    else:
        # redirect to long url
        return HttpResponseRedirect(urlSet[0].long_url)

def index(request):
    return HttpResponse("Hello, world. You're at the urls index.")

''' ============ HELPER METHODS ============ '''

BASE_62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_base_62(id):
    base10 = int(id)
    base62 = ''
    while base10 != 0:
        base62 = BASE_62[base10 % 62] + base62
        base10 = base10 / 62
    return base62

def to_base_10(base62):
    base10 = 0
    for ch in base62:
        base10 = base10 * 62 + BASE_62.index(ch)
    return base10
