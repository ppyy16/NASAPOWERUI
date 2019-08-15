from django.http import HttpResponse
#combines a given template, with a given context and returns an object with that rendered stuff
from django.shortcuts import render
from .models import dummy
from django.views.generic import TemplateView
# Create your views here.
#handles various webpages

#VIEWS: Takes a web request, and handles it to turn it into a response
#context: a minimal set of data used by a task, may be used to save as a point to return to in cases of failure
#django templates, when rendered are compiled once and then kept as an optimization
#context is a dictionary, where the instances of the key are replaced by the value

def home_view(request,*args, **kwargs):
	info = dummy.objects.all()
	print(info)
	return render(request, "home.html", {'info': info})






