from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# from .models import Character, Room
from .actions import MakeAttack
import requests, os



def landing(request):
    return render(request, 'site/landing.html')


class lobby(ListView):
    model = 'fake room'
    # template_name = 'site/lobby.html'
    # context_object_name = 'rooms'
    # ordering = ['-date_created']


class room(ListView):
    model = 'fake room'
    template_name = 'site/room.html'
    text_object_name = 'room'


@login_required
def create_item(request):
    return render(request, 'create/item.html')


@login_required
def create_npc(request):
    return render(request, 'create/npc.html')


@login_required
def create_pc(request):
    return render(request, 'create/pc.html')


@login_required
def create_room(request):
    return render(request, 'create/room.html')


@login_required
def create(request):
    return render(request, 'create/create.html')