from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import PlaceTestSerializer
from .models import Place
def create_5000_place(request):
	i=0
	while 5000>i:
		Place.objects.create(name_place ='Test',description = 'wqdwdwqdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',location='0,0')
		i=i+1
	return HttpResponse("5000 est")

def return_place_5000(request):
	plces = Place.objects.all()
	serializer = PlaceTestSerializer(plces, many=True)
	return JsonResponse(serializer.data, safe=False)