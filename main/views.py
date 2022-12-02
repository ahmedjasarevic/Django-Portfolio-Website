from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib import messages
from .forms import NewUserForm





def contact(request):
    return render(request,"main/contact.html")

def homepage(request):
    return render(request,"main/home.html")


def projects(request):
    return render(request,"main/projects.html")