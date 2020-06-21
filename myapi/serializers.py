from rest_framework import serializers

from .models import Event,PlaceEntertaiment,News,Poster,CategoryEntertaiment,CategoryOrder,CategorySearch,PlaceOrder,PlaceSearch


class EventSerializer(serializers.ModelSerializer):
	location_place = serializers.ReadOnlyField()
	location_name = serializers.ReadOnlyField()
	class Meta:
		model = Event
		fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all__'

class PosterSerializer(serializers.ModelSerializer):
	location_place = serializers.ReadOnlyField()
	location_name = serializers.ReadOnlyField()
	class Meta:
		model = Poster
		fields = '__all__'
		
class CategoryEntSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryEntertaiment
		fields = '__all__'

class CategoryOrdSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryOrder
		fields = '__all__'

class CategorySearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategorySearch
		fields = '__all__'

class PlaceSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlaceSearch
		fields = '__all__'

class PlaceEntertaimentSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlaceEntertaiment
		fields = '__all__'

class PlaceOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlaceOrder
		fields = '__all__'


		


			
		