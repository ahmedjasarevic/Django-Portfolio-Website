from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries, TutorialImage
from django.contrib import messages
from .forms import NewUserForm





def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":Tutorial.objects.all})

def contact(request):
    return render(request,"main/contact.html")


def about(request):
    return render(request,"main/about.html",
                  context={"tutorials": Tutorial.objects.all})




def projects(request):
    return render(request = request,
                  template_name='main/projects.html',
                  context = {"tutorials":Tutorial.objects.all})

def detail(request, slug):
    post = Tutorial.objects.get(tutorial_slug=slug)
    photos = TutorialImage.objects.filter(post=post)
    return render(request, 'main/projectsDetails.html', {'post': post, 'photos': photos})

