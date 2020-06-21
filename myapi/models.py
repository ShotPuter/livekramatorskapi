from django.db import models
from django_resized import ResizedImageField #Импортируем библиотеку для изменения размера изображений
from django.utils.encoding import python_2_unicode_compatible
#from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.db import models
from location_field.models.plain import PlainLocationField
from django import forms
from django.contrib.auth.models import User
from vote.models import VoteModel


#############__Модель карты__################

#class Migration(migrations.Migration):
#	operations = [
#		CreateExtension('postgis'),
#	]
#__________________________________________________________________________________________________________________________________________#

#############__Модель категории_развлечения_################
@python_2_unicode_compatible
class CategoryEntertaiment(models.Model):
	name = models.CharField(u'Название',max_length=200)
	image = models.ImageField(u'Изображение',upload_to='category_image')
	class Meta:
		verbose_name = u"Категория развлечений"
		verbose_name_plural = u"Категории развлечений"
	def __str__(self):
		return '%s' % (self.name)

#__________________________________________________________________________________________________________________________________________#

#############__Модель категории_заказать_################
@python_2_unicode_compatible
class CategoryOrder(models.Model):
	name = models.CharField(u'Название',max_length=200)
	image = models.ImageField(u'Изображение',upload_to='category_image')
	class Meta:
		verbose_name = u"Категория заказать"
		verbose_name_plural = u"Категории заказать"
	def __str__(self):
		return '%s' % (self.name)

#__________________________________________________________________________________________________________________________________________#

#############__Модель категории_найти_################
@python_2_unicode_compatible
class CategorySearch(models.Model):
	name = models.CharField(u'Название',max_length=200)
	class Meta:
		verbose_name = u"Категория поиска"
		verbose_name_plural = u"Категории поиска"
	def __str__(self):
		return '%s' % (self.name)

#__________________________________________________________________________________________________________________________________________#

#############__Модель места развлечения __################
@python_2_unicode_compatible
class PlaceEntertaiment(VoteModel,models.Model):
	name_place = models.CharField(u'Название',max_length=500)
	description = models.TextField(u'Описание',blank=True)
	tel = models.CharField(u'Телефон',blank=True,max_length=100)
	adress = models.CharField(u'Адрес',blank=True,max_length=200)
	working_time = models.CharField(u'Время работы',blank=True,max_length=100)
	small_img = ResizedImageField(u'Миниатюра',size=[640, 320], crop=['middle', 'center'], upload_to='photos',blank=True)
	high_img = ResizedImageField(u'Полное фото',size=[1280, 720], crop=['middle', 'center'], upload_to='photos',blank=True)
	special_offers = models.IntegerField(u'Количество предложений',default=1)
	link = models.CharField(u'Ссылка',max_length=500,blank=True)
	location = PlainLocationField(based_fields=['city'], zoom=7,default='48.737512197810915,397.5847434997558')

	top = models.BooleanField(u'Топ',blank=True)
	category = models.ForeignKey(CategoryEntertaiment,verbose_name=u'Категория',default = 1,on_delete=models.CASCADE,blank=True)


	class Meta:
		verbose_name = u"Развлечение"
		verbose_name_plural = u"Развлечения"
	def __str__(self):
		return '%s' % (self.name_place)
	
#___________________________________________________________________________________________________________________________________________#


#############__Модель места Заказать __################
@python_2_unicode_compatible
class PlaceOrder(VoteModel,models.Model):
	name_place = models.CharField(u'Название',max_length=500)
	description = models.TextField(u'Описание',blank=True)
	tel = models.CharField(u'Телефон',blank=True,max_length=100)
	adress = models.CharField(u'Адрес',blank=True,max_length=200)
	working_time = models.CharField(u'Время работы',blank=True,max_length=100)
	small_img = ResizedImageField(u'Миниатюра',size=[640, 320], crop=['middle', 'center'], upload_to='photos',blank=True)
	high_img = ResizedImageField(u'Полное фото',size=[1280, 720], crop=['middle', 'center'], upload_to='photos',blank=True)
	link = models.CharField(u'Ссылка',max_length=500,blank=True)
	category = models.ForeignKey(CategoryOrder,verbose_name=u'Категория',default = 1,on_delete=models.CASCADE,blank=True)

	class Meta:
		verbose_name = u"Заказать"
		verbose_name_plural = u"Заказать"
	def __str__(self):
		return '%s' % (self.name_place)
	
#___________________________________________________________________________________________________________________________________________#

#############__Модель места Найти __################
@python_2_unicode_compatible
class PlaceSearch(models.Model):
	name_place = models.CharField(u'Название',max_length=500)
	adress = models.CharField(u'Адрес',blank=True,max_length=200)
	working_time = models.CharField(u'Время работы',blank=True,max_length=100)
	category = models.ForeignKey(CategorySearch,verbose_name=u'Категория',default = 1,on_delete=models.CASCADE,blank=True)
	location = PlainLocationField(based_fields=['city'], zoom=7,default='48.737512197810915,397.5847434997558')
	class Meta:
		verbose_name = u"Найти"
		verbose_name_plural = u"Найти"
	def __str__(self):
		return '%s' % (self.name_place)
	
#___________________________________________________________________________________________________________________________________________#


#############__Модель Маршрут__################

class Way(models.Model):
	name = models.CharField(u'Название',max_length=500)
	pk_way = models.CharField(u'Передаваемое имя',max_length=30)
	class Meta:
		verbose_name = u"Маршрут"
		verbose_name_plural = u"Маршруты"
#____________________________________________________________________________________________________________________________________________#

#############__Модель Координаты__################
#Связь с моделью Маршрут
class Koordinates(models.Model):
	way = models.ForeignKey(Way)
	city = models.CharField(u'Координаты',max_length=1000,default='48.737512197810915,397.5847434997558')
	stop = PlainLocationField(based_fields=['stoped'], zoom=7)
	length = models.FloatField()
	width = models.FloatField()
	

#____________________________________________________________________________________________________________________#

#############__Модель мероприятия__################

class Event(models.Model):
	name = models.CharField(u'Название',max_length=200)
	text = models.TextField(u'Текст')
	date = models.DateField(u'Дата сортировки')     #Дата сортировки по времени
	link = models.CharField(u'Источник',max_length=1000)
	card = models.ImageField(u'Миниатюра',upload_to='photos', blank=True, null=True)
	photo = ResizedImageField(u'Полное фото',size=[1280, 720], crop=['middle', 'center'], upload_to='photos')
	place_loc = models.ForeignKey(PlaceEntertaiment,verbose_name=u'Место',default = 1,on_delete=models.CASCADE)# Связь с моделью места, расскоментировать когда будет место
	class Meta:
		verbose_name = u"Мероприятие"
		verbose_name_plural = u"Мероприятия"

	@property
	def location_place(self):
		return  self.place_loc.location

	@property
	def location_name(self):
		return  self.place_loc.name_place
		
#_____________________________________________________________________________________________________________________________________________#

#############__Модель новости__################


class News(models.Model):
	name = models.CharField(u'Название',max_length=200)
	text = models.TextField(u'Текст')
	Police = 'Police'
	Sport = 'Sport'
	Live = 'Live'
	GA = 'GorAdmin'
	City = 'City'
	Study = 'Study'
	Important = 'Important'
	NEWS_CHOICES = (
		(Police, u'Полиция'),
		(Sport, u'Спорт'),
		(Live, u'Общественная жизнь'),
		(GA, u'Городская администрация'),
		(City, u'Благоустройство города'),
		(Study, u'Образование'),
		(Important, u'Важное'),
		)
	news_choice = models.CharField(max_length=100,choices=NEWS_CHOICES,default=Live)
	date = models.DateField(u'Дата')     #Дата сортировки по времени
	link = models.CharField(u'Источник',max_length=1000)
	card = models.ImageField(u'Миниатюра',upload_to='photos', blank=True, null=True)
	photo = ResizedImageField(u'Полное фото',size=[1280, 720], crop=['middle', 'center'], upload_to='photos')
	class Meta:
		verbose_name = u"Новость"
		verbose_name_plural = u"Новости"
#____________________________________________________________________________________________________________________#

#############__Модель Афиша__################


class Poster(models.Model):
	Kino = 'Kino'
	Concert = 'Concert'
	Teatr = 'Teatr'
	name = models.CharField(u'Название',max_length=500)
	POSTER_CHOICE =(
		(Kino, u'Кино'),
		(Concert, u'Концерт'),
		(Teatr, u'Театр'),
		)
	vid = models.CharField(u'Вид постера',max_length=500,choices=POSTER_CHOICE)
	description = models.TextField(u'Описание')
	types = models.CharField(u'Жанры',max_length=500)
	actors = models.TextField(u'Актеры')
	seans = models.TextField(u'Сеансы')
	language = models.CharField(u'Язык показа',max_length=500)
	time = models.CharField(u'Время показа',max_length=500)
	cost = models.CharField(u'Цена показа',max_length=100)
	date = models.CharField(u'Дата',max_length=100)
	link = models.CharField(u'YouTube',max_length=1000)
	photo = models.ImageField(u'Постер фото',upload_to='photos', blank=True, null=True)
	full_photo = ResizedImageField(u'Полное фото',size=[1280, 720], crop=['middle', 'center'], upload_to='photos')
	place_loc = models.ForeignKey(PlaceEntertaiment,verbose_name=u'Место',default = 1)# Связь с моделью места
	class Meta:
		verbose_name = u"Постер"
		verbose_name_plural = u"Афиша"	
	@property
	def location_place(self):
		return  self.place_loc.location

	@property
	def location_name(self):
		return  self.place_loc.name_place
#____________________________________________________________________________________________________________________#

#############__Форма маршрута__################
# Имя маршрута
class WayForm(forms.Form):
	pk_name = forms.CharField(label='pk_name', max_length=100)
#____________________________________________________________________________________________________________________#

#############__Форма новостей__################
#Для каждого значение 0 или 1
class NewsForm(forms.Form): 
	police = forms.IntegerField()
	sport = forms.IntegerField()
	live = forms.IntegerField()
	ga = forms.IntegerField()
	city = forms.IntegerField()
	study = forms.IntegerField()
	important = forms.IntegerField()
#____________________________________________________________________________________________________________________#

#############__Форма категории__################
# Имя маршрута
class CategoryForm(forms.Form):
	search = forms.IntegerField()
	entertaiment = forms.IntegerField()
	order = forms.IntegerField()
#____________________________________________________________________________________________________________________#

#############__Форма выбора категории и отдача мест в этой категории__################
class CategoryIdForm(forms.Form):
	id_category = forms.CharField(label='id_category', max_length=1000)
	
#____________________________________________________________________________________________________________________#

#############__Форма выбора категории и отдача мест в этой категории__################
class PlaceIdForm(forms.Form):
	id_place = forms.CharField(label = 'id_place', max_length=100)
	token_user = forms.CharField(label = 'token_user', max_length=500)
#____________________________________________________________________________________________________________________#

class SearchForm(forms.Form):
	search_field = forms.CharField(label = 'search_field', max_length=500)