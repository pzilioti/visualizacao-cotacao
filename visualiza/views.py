from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .service import ValidationService


def index(request):
	svc = ValidationService()
	if(svc.is_valid()):
		values_list = svc.get_list_values()
		return HttpResponse(f"Valid!!! {values_list}")
	else:
		return HttpResponse("Invalid!!")


def partial(request, currency):
	svc = ValidationService(currency=currency)
	if(svc.is_valid()):
		return HttpResponse(f"Test. Currency: {currency}")
	else:
		return HttpResponse(f"Invalid!! {currency}")


def full(request, currency, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%Y%m%d")
		end_date = datetime.strptime(end_date, "%Y%m%d")
		svc = ValidationService(currency=currency, start_date=start_date, end_date=end_date)
		if(svc.is_valid()):
			return HttpResponse(f"Test. Currency: {currency}, from {start_date} to {end_date}")
		else:
			return HttpResponse(f"Invalid!! {currency},  from {start_date} to {end_date}")
	except ValueError as err:
		return HttpResponse(f"Test - Invalid date format. Currency: {currency}, from {start_date} to {end_date}")

	

