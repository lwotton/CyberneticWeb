from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from map.models import Citizen, Location

class Index(View):

	def get(self,request):
	
   		latest_locations_one = Location.objects.filter(citizen_id="1")
   		latest_locations_two = Location.objects.filter(citizen_id="2")
    	
    		return render(request, 'map/index.html', {'latest_locations_one':latest_locations_one,'latest_locations_two':latest_locations_two})
