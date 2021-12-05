from django.core import serializers
from datetime import datetime, timedelta
import logging
import sys
import requests
from .utils import validate_dates, validate_currency
from .models import Quotation

class ValidationService():
	logging.basicConfig(format='%(asctime)s %(message)s', stream=sys.stdout, level=logging.DEBUG)

	def __init__(self, currency=None, start_date=None, end_date=None):
		currency = currency if currency else "BRL"
		end_date = end_date if end_date else datetime.now().date()
		#if current day is in a weekend, the number os days to subtract to get 5 workdays should be greater than 5
		#if current day is saturday it will subtract 6 days, is it's a sunday, it will subtract 7 days
		#this way the default dates when none is given should always be right
		num_day = 5 + (end_date.weekday() - 4 if end_date.weekday() in [5,6] else 0)
		start_date = start_date if start_date else datetime.now().date() - timedelta(days=num_day)
		
		self.start_date, self.end_date = validate_dates(start_date, end_date)
		self.currency = validate_currency(currency)
		
	def is_valid(self):
		if(self.currency and self.start_date and self.end_date):
			return True
		else:
			return False

	def get_list_values(self):
		values_list = []
		aux_date = self.end_date
		while(aux_date >= self.start_date):
			value = self.__get_values_from_db(aux_date, self.currency)
			if (not value):
				logging.debug(f"Date {aux_date} for {self.currency} still does not exists in DB. Getting from API")
				value = self.__get_values_from_api(aux_date, self.currency)
			values_list.append(value)
			aux_date = aux_date - timedelta(days=1)
		
		return serializers.serialize('json', values_list)

	def __get_values_from_db(self, date, currency):
		try:
			result = Quotation.objects.filter(date=date, currency=currency).get()
			logging.debug(result)
			return result
		except Quotation.DoesNotExist as err:
			return None
		
		
	def __get_values_from_api(self, date, currency):
		r = requests.get(f'https://api.vatcomply.com/rates?base=USD&date={date.strftime("%Y-%m-%d")}')
		if(r.status_code == 200):	
			logging.debug("Success getting from API")
			data = r.json()
			#saves all currencies, not only the current one
			eur = Quotation(date=date, currency="EUR", value=data.get("rates").get("EUR"))
			eur.save()
			jpy = Quotation(date=date, currency="JPY", value=data.get("rates").get("JPY"))
			jpy.save()
			brl = Quotation(date=date, currency="BRL", value=data.get("rates").get("BRL"))
			brl.save()

			if(currency=="EUR"): return eur
			if(currency=="JPY"): return jpy
			if(currency=="BRL"): return brl
		else:
			logging.warning("Error in API")
			return None

		