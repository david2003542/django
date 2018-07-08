from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Member

def register(request):
    """"""

def activate(request, code):
    """"""

def login(request, uuid):
    """"""

def login(request, uuid):
    """"""

def profile(request, uuid):
    member = get_object_or_404(Member, uuid=uuid)
    return render(request, 'member/profile.html', {'member': member})

