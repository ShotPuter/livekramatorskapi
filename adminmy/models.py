from django.db import models


class DescriptionVersion(models.Model):
	name = models.CharField(u"Название",max_length=200)
	version = models.CharField(u"Версия",max_length=200)
	text = models.TextField(u"Текст")
	date = models.DateField(u"Дата")
	class Meta:
		verbose_name = u"Верссия сервера"
		verbose_name_plural = u"Версии сервера"
		