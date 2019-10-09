from django.shortcuts import render
from django.http import HttpResponse

import requests
import os

def index(request):
    return render(request, 'knuckledragger/index.html')