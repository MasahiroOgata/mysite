from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message' : 'Welcome my BBS',
    }
    return render(request, 'bbs/index.html', context)