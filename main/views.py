from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib import messages
from .forms import NewUserForm



def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":TutorialCategory.objects.all})

def contact(request):
    return render(request,"main/contact.html")