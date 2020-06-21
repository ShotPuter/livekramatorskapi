from django.conf.urls import url,include
from .views import SearchFunc,out_event,poisk_mr,poisknews_bd,choice_category,choice_search, choice_enter_place,out_poster,like_enter_place, choice_order_place,  like_order_place,check_like_ent,check_like_order

urlpatterns = [ url("events/",out_event),
				url("route/",poisk_mr),
				url("news/",poisknews_bd),
				url("razdel/",choice_category),
				url("get-entertaiment/",choice_enter_place),
				url("get-order/",choice_order_place),
				url("posters/",out_poster),
				url("like-ent/",like_enter_place),
				url("like-ord/",like_order_place),
				url("check-order-place/",check_like_order),
				url("check-entertaiment-place/",check_like_ent),
				url("search/",SearchFunc),
				url("search-get/",choice_search)
				

				
				
				
]