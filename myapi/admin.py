from django.contrib import admin


from myapi.models import Event,PlaceEntertaiment, PlaceOrder,Way,Koordinates,News,Poster, CategoryEntertaiment, PlaceSearch, CategorySearch, CategoryOrder
class NewsEventAdmin(admin.ModelAdmin):
	list_display=['name']

class PlaceSearchAdmin(admin.ModelAdmin):
	list_display=['name_place']

class KordiWay(admin.StackedInline):
	model = Koordinates
	extra = 4
class WayAdmin(admin.ModelAdmin):
	list_display=['name']
	inlines = [KordiWay]	
	

class PlaceEntertaimentAdmin(admin.ModelAdmin):
	list_display=['name_place']
	fieldsets = (
        (None, {
            'fields': ('category' ,'name_place',('small_img',),'description','location', )
        }),
        (u'Информация', {
            'classes': ('collapse',),
            'fields': (('working_time','tel',),'adress','high_img','link',),
        }),
        (u'Реклама', {
            'classes': ('collapse',),
            'fields': ('top',),
        }),
    )

class PlaceOrderAdmin(admin.ModelAdmin):
	list_display=['name_place']
	fieldsets = (
        (None, {
            'fields': ('category' ,'name_place',('small_img',),'description')
        }),
        (u'Информация', {
            'classes': ('collapse',),
            'fields': (('working_time','tel',),'adress','high_img','link',),
        }),
    )
admin.site.register(PlaceSearch,PlaceSearchAdmin)
admin.site.register(PlaceEntertaiment,PlaceEntertaimentAdmin)
admin.site.register(PlaceOrder,PlaceOrderAdmin)
admin.site.register(Event,NewsEventAdmin)
admin.site.register(Way,WayAdmin)
admin.site.register(News,NewsEventAdmin)
admin.site.register(Poster,NewsEventAdmin)
admin.site.register(CategoryEntertaiment,NewsEventAdmin)
admin.site.register(CategoryOrder,NewsEventAdmin)
admin.site.register(CategorySearch,NewsEventAdmin)

