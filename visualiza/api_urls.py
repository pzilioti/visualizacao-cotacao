from django.urls import path

from . import api_views

urlpatterns = [
	path('', api_views.index, name='api_index'),
	path('<str:currency>/', api_views.partial, name='api_partial'),
	path('<str:currency>/<str:start_date>/<str:end_date>', api_views.full, name='api_full'),
	
]