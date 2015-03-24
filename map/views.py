from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from map.models import Citizen, Location
from django_ajax.decorators import ajax

class Index(View):

	def get(self,request):
	
   		latest_locations = Location.objects.all()
    	
    		return render(request, 'map/index.html', {'latest_locations':latest_locations})

@ajax
def my_view(request):

    latest_locations_one_test = Location.objects.all()
    return {latest_locations_one_test}