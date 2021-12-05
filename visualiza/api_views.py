import json, logging, sys
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .service import ApiService


def index(request, date):
	logging.basicConfig(format='%(asctime)s %(message)s', stream=sys.stdout, level=logging.DEBUG)
	try:
		date = datetime.strptime(date, "%Y%m%d").date()
		svc = ApiService(date=date)
	
		return JsonResponse(svc.get_rates_from_db())
	except Exception as err:
		logging.error(err)
		return JsonResponse({"error": "Invalid"})


