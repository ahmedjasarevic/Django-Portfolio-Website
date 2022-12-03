from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib import messages
from .forms import NewUserForm





def contact(request):
    return render(request,"main/contact.html")


def about(request):
    return render(request,"main/about.html")

def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":Tutorial.objects.all})



def projects(request):
    return render(request = request,
                  template_name='main/projects.html',
                  context = {"tutorials":Tutorial.objects.all})

