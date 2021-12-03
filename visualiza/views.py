from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .service import Service


def index(request):
	svc = Service()
	if(svc.is_valid()):
		return HttpResponse("Valid!!!")
	else:
		return HttpResponse("Invalid!!")


def partial(request, currency):
	svc = Service(currency=currency)
	if(svc.is_valid()):
		return HttpResponse(f"Test. Currency: {currency}")
	else:
		return HttpResponse(f"Invalid!! {currency}")


def full(request, currency, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%Y%m%d")
		end_date = datetime.strptime(end_date, "%Y%m%d")
		svc = Service(currency=currency, start_date=start_date, end_date=end_date)
		if(svc.is_valid()):
			return HttpResponse(f"Test. Currency: {currency}, from {start_date} to {end_date}")
		else:
			return HttpResponse(f"Invalid!! {currency},  from {start_date} to {end_date}")
	except ValueError as err:
		return HttpResponse(f"Test - Invalid date format. Currency: {currency}, from {start_date} to {end_date}")

	

