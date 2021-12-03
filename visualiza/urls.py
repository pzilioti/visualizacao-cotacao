from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:currency>/', views.partial, name='partial'),
	path('<str:currency>/<str:start_date>/<str:end_date>', views.full, name='full'),
	
]