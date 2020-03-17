from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    # get all Job objects from database and turn them to python objects
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs' : jobs})