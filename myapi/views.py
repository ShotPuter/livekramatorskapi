from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core import serializers
from .models import Event,Way,Koordinates,WayForm,News,NewsForm,Poster, CategoryEntertaiment,CategoryOrder,CategorySearch,CategoryIdForm , PlaceSearch ,PlaceEntertaiment, PlaceOrder ,CategoryForm, PlaceIdForm, SearchForm
from .serializers import EventSerializer, NewsSerializer, PosterSerializer,CategoryEntSerializer,CategoryOrdSerializer,CategorySearchSerializer, PlaceEntertaimentSerializer, PlaceOrderSerializer, PlaceSearchSerializer
import json
from rest_framework.authtoken.models import Token
from userapi.models import User
from rest_framework import filters
from rest_framework import generics
######################__Метод отдачи мероприятий(Get)__#################
@csrf_exempt
def out_event(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
    else: 
        return HttpResponse("Ne tot method")
#_________________________________________________________________________________________________________________________________________#

######################__Метод отдачи постера(Get)__#################
@csrf_exempt
def out_poster(request):
    if request.method == 'GET':
        posters = Poster.objects.order_by('-id')
        serializer = PosterSerializer(posters, many=True)
        return JsonResponse(serializer.data, safe=False)
    else: 
        return HttpResponse("Ne tot method")
#_________________________________________________________________________________________________________________________________________#        

######################__Метод отдачи маршрута(POST)__#################
@csrf_exempt
def poisk_mr(request):
    if request.method == 'POST':
        form = WayForm(request.POST)
        if form.is_valid():
            pk_name = form.cleaned_data.get('pk_name')
            coord = Koordinates.objects.filter(way=Way.objects.filter(pk_way=pk_name))
            return HttpResponse(serializers.serialize('json', coord), content_type="application/json") 
        else:
        	 pk_name = form.cleaned_data.get('pk_name')
        	 return HttpResponse("Ne proshla valid %s" %(pk_name))
    else:
        	 return HttpResponse("Ne tot metod")
#_________________________________________________________________________________________________________________________________________#

@csrf_exempt  
def poisknews_bd(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			intpolice = form.cleaned_data.get('police')
			intsport = form.cleaned_data.get('sport')
			intlive = form.cleaned_data.get('live')
			intga = form.cleaned_data.get('ga')
			intcity = form.cleaned_data.get('city')
			intstudy = form.cleaned_data.get('study')
			intimportant = form.cleaned_data.get('important')
			if (intpolice == 1) and (intsport == 1) and (intlive == 1) and (intga==1) and (intcity==1) and (intstudy == 1) and (intimportant == 1):
				news=News.objects.order_by('-date')
				serializer = NewsSerializer(news,many=True)
				return JsonResponse(serializer.data, safe=False)
			else:
				news = News.objects.all()

				if intpolice == 0:
					news = news.exclude(news_choice='Police')

				if intsport == 0:
					news =news.exclude(news_choice='Sport')

				if intlive == 0:
					news =news.exclude(news_choice='Live')

				if intga == 0:
					news =news.exclude(news_choice='GorAdmin')

				if intcity == 0:
					news =news.exclude(news_choice='City')

				if intstudy == 0:
					news =news.exclude(news_choice='Study')

				if intimportant == 0:
					news = news.exclude(news_choice='Important')
				
				serializer = NewsSerializer(news.order_by('-date'),many=True)
				return JsonResponse(serializer.data, safe=False)   
		else:	 
			return HttpResponse("Forma ne proshla validaciu ")
	else:
		return HttpResponse("Ne tot metod zaprosa")
#_________________________________________________________________________________________________________________________________________#

######################__Метод отдачи категории из подраздела(POST)__#################
@csrf_exempt
def choice_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			intsearch = form.cleaned_data.get('search')
			intentertaiment = form.cleaned_data.get('entertaiment')
			intorder = form.cleaned_data.get('order')
			

			if intsearch == 1:
				category_mas = CategorySearch.objects.all()
				serializer = CategorySearchSerializer(category_mas,many=True)

			if intentertaiment == 1:
				category_mas = CategoryEntertaiment.objects.all()
				serializer = CategoryEntSerializer(category_mas,many=True)

			if intorder == 1:
				category_mas = CategoryOrder.objects.all()
				serializer = CategoryOrdSerializer(category_mas,many=True)

			
			return JsonResponse(serializer.data, safe=False) 

		else:	 
			return HttpResponse("Forma ne proshla validaciu ")
	else:
		return HttpResponse("Ne tot metod zaprosa")
#_________________________________________________________________________________________________________________________________________#

######################__Метод отдачи мест из категории(POST)__#################  //////////// Переделать на раздельное///////////////
@csrf_exempt
def choice_enter_place(request):
	if request.method == 'POST':
		form = CategoryIdForm(request.POST)
		if form.is_valid():
			id_category = form.cleaned_data.get('id_category')
			place_mas = PlaceEntertaiment.objects.filter(category=CategoryEntertaiment.objects.filter(id=id_category))
			serializer = PlaceEntertaimentSerializer(place_mas.order_by('-top'),many=True)
			return JsonResponse(serializer.data, safe=False) 

		else:	 
			return HttpResponse("Forma ne proshla validaciu ")
	else:
		return HttpResponse("Ne tot metod zaprosa")





@csrf_exempt
def choice_order_place(request):
    if request.method == 'POST':
        form = CategoryIdForm(request.POST)
        if form.is_valid():
            id_category = form.cleaned_data.get('id_category')
            place_mas = PlaceOrder.objects.filter(category=CategoryOrder.objects.filter(id=id_category))
            serializer = PlaceOrderSerializer(place_mas.order_by('-id'),many=True)
            
            return JsonResponse(serializer.data, safe=False) 

        else:    
            return HttpResponse("Forma ne proshla validaciu ")
    else:
        return HttpResponse("Ne tot metod zaprosa")


@csrf_exempt
def check_like_ent(request):
    if request.method == 'POST':
        form = PlaceIdForm(request.POST)
        if form.is_valid():
            id_place = form.cleaned_data.get('id_place')
            token_user = form.cleaned_data.get('token_user')
            if token_user == "Null" or token_user == "null":
                dict_place = json.dumps({
                "total_like": place.vote_score,
                "islike": None
                })
            else:
                key_token = Token.objects.get(key=token_user)
                usr_token = User.objects.get(email=key_token.user)
                id_user = usr_token.id 
                place = PlaceOrder.objects.get(id=id_place)
                islike = place.votes.exists(id_user)
                dict_place = json.dumps({
                "total_like": place.vote_score,
                "islike": islike
                })
            return HttpResponse(dict_place, content_type="application/json")  #serializers.serialize('json', dict_place),
        else:
             return HttpResponse("Ne proshla valid " )
    else:
             return HttpResponse("Ne tot metod")


@csrf_exempt
def check_like_order(request):
    if request.method == 'POST':
        form = PlaceIdForm(request.POST)
        if form.is_valid():
            id_place = form.cleaned_data.get('id_place')
            token_user = form.cleaned_data.get('token_user')

            if token_user == "Null" or token_user == "null":
                dict_place = json.dumps({
                "total_like": place.vote_score,
                "islike": None
                })
            else:
                key_token = Token.objects.get(key=token_user)
                usr_token = User.objects.get(email=key_token.user)
                id_user = usr_token.id 
                place = PlaceOrder.objects.get(id=id_place)
                islike = place.votes.exists(id_user)
                dict_place = json.dumps({
                "total_like": place.vote_score,
                "islike": islike
                })
            return HttpResponse(dict_place, content_type="application/json")  #serializers.serialize('json', dict_place),
        else:
             return HttpResponse("Ne proshla valid " )
    else:
             return HttpResponse("Ne tot metod")


    

@csrf_exempt
def like_enter_place(request):
    if request.method == 'POST':
        form = PlaceIdForm(request.POST)
        if form.is_valid():
            id_place = form.cleaned_data.get('id_place')
            token_user = form.cleaned_data.get('token_user')
            key_token = Token.objects.get(key=token_user)
            usr_token = User.objects.get(email=key_token.user)
            id_user = usr_token.id 
            place = PlaceEntertaiment.objects.get(id=id_place)
            if place.votes.exists(id_user) == True:
                place.votes.delete(id_user)
                status=True
                eror = None
                islike = False
            else:
                place.votes.up(id_user)
                status = True
                eror = None
                islike = True
            dict_place = json.dumps({
                "error": eror,
                "status": status,
                "islike": islike,
                })
            return HttpResponse(dict_place, content_type="application/json")
        else:
        	 return HttpResponse("Ne proshla valid " )
    else:
        	 return HttpResponse("Ne tot metod")


@csrf_exempt
def like_order_place(request):
    if request.method == 'POST':
        form = PlaceIdForm(request.POST)
        if form.is_valid():
            id_place = form.cleaned_data.get('id_place')
            token_user = form.cleaned_data.get('token_user')
            key_token = Token.objects.get(key=token_user)
            usr_token = User.objects.get(email=key_token.user)
            id_user = usr_token.id 
            place = PlaceOrder.objects.get(id=id_place)
            if place.votes.exists(id_user) == True:
                place.votes.delete(id_user)
                status=True
                eror = None
                islike = False
            else:
                place.votes.up(id_user)
                status = True
                eror = None
                islike = True
            dict_place = json.dumps({
                "error": eror,
                "status": status,
                "islike": islike,
                })
            return HttpResponse(dict_place, content_type="application/json")

        else:
             return HttpResponse("Ne proshla valid " )
    else:
             return HttpResponse("Ne tot metod")


def SearchFunc(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search_field')
            place_mas1 = list(PlaceSearch.objects.filter(name_place__contains=search))
            place_mas2 = list(PlaceEntertaiment.objects.filter(name_place__contains=search))
            place_mas = place_mas1+place_mas2
            serializer = PlaceSearchSerializer(place_mas,many=True)
            return JsonResponse(serializer.data, safe=False) 

        else:    
            return HttpResponse("Forma ne proshla validaciu ")
    else:
        return HttpResponse("Ne tot metod zaprosa")
    



@csrf_exempt
def choice_search(request):
    if request.method == 'POST':
        form = CategoryIdForm(request.POST)
        if form.is_valid():
            id_category = form.cleaned_data.get('id_category')
            place_mas = PlaceSearch.objects.filter(category=CategorySearch.objects.filter(id=id_category))
            serializer = PlaceSearchSerializer(place_mas.order_by('-id'),many=True)
            return JsonResponse(serializer.data, safe=False) 

        else:    
            return HttpResponse("Forma ne proshla validaciu ")
    else:
        return HttpResponse("Ne tot metod zaprosa")
