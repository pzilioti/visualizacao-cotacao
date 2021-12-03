from django.urls import path

from . import api_views

urlpatterns = [
	path('', api_views.index, name='index'),
	path('<str:currency>/', api_views.partial, name='partial'),
	path('<str:currency>/<str:start_date>/<str:end_date>', api_views.full, name='full'),
	
]