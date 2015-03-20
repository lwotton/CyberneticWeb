from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from map.models import Citizen, Location

class Index(View):

	def get(self,request):
	
   		latest_locations = Location.objects.all()
    	
    		context = {'latest_locations': latest_locations}
    	
    		return render(request, 'map/index.html', context)

