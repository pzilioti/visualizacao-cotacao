from django.urls import path

from . import api_views

urlpatterns = [
	path('<str:date>/', api_views.index, name='api_index'),
]