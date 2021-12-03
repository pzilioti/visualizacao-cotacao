from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("API No arguments")

def partial(request, currency):
    return HttpResponse(f"API Test. Currency: {currency}")

def full(request, currency, start_date, end_date):
    return HttpResponse(f"API Test. Currency: {currency}, from {start_date} to {end_date}")
