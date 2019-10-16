from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Character, Room
from .actions import MakeAttack
import requests, os


@login_required
def index(request):
    return render(request, 'site/index.html')


@login_required
def lobby(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'site/lobby.html', context)


class lobby(ListView):
    model = Room
    template_name = 'site/lobby.html'
    context_object_name = 'rooms'
    # ordering = ['-date_created']


@login_required
def test(request):
    return render(request, 'site/test/test.html')


# Inside this file, the view, we are going to import our forms.
# We will use that form inside the request 'attack'
