from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.utils.importlib import import_module
from django.shortcuts import render_to_response,get_object_or_404
import models

def aindex(request):
	query = {'shouts':models.aShout.objects.all()}
	return render_to_response('index.html',query)

def ashowpost(request,slug):
	query = {'shout':models.aShout.objects.get(slug = slug)}
	#query = {'shouts' : get_object_or_404(models.aShout,slug = slug)}
	return render_to_response('showpost.html',query)
