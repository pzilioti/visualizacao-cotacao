from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .service import ValidationService


def index(request):
	try:
		currency = request.POST.get('currency', None)
		start_date = request.POST.get('startDateInput', None)
		end_date = request.POST.get('endDateInput', None)
		if(start_date): start_date = datetime.strptime(start_date[:10], "%d/%m/%Y").date()
		if(end_date): end_date = datetime.strptime(end_date[:10], "%d/%m/%Y").date()
	except Exception as err:
		pass
	
	svc = ValidationService(currency=currency, start_date=start_date, end_date=end_date)
	if(svc.is_valid()):
		values_list = svc.get_list_values()
		context = {'values_list': values_list}
		return render(request, 'visualiza/index.html', context)
	else:
		return HttpResponse("Invalid!!")


def partial(request, currency):
	svc = ValidationService(currency=currency)
	if(svc.is_valid()):
		values_list = svc.get_list_values()
		context = {'values_list': values_list}
		return render(request, 'visualiza/index.html', context)
	else:
		return HttpResponse("Invalid!!")


def full(request, currency, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%Y%m%d").date()
		end_date = datetime.strptime(end_date, "%Y%m%d").date()
		svc = ValidationService(currency=currency, start_date=start_date, end_date=end_date)
		if(svc.is_valid()):
			values_list = svc.get_list_values()
			context = {'values_list': values_list}
			return render(request, 'visualiza/index.html', context)
		else:
			return HttpResponse("Invalid!!")
	except ValueError as err:
		return HttpResponse(f"Test - Invalid date format. Currency: {currency}, from {start_date} to {end_date}")
