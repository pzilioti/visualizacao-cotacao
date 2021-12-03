from datetime import datetime, timedelta
import logging
import sys
from .utils import validate_dates, validate_currency

class Service():
	logging.basicConfig(format='%(asctime)s %(message)s', stream=sys.stdout, level=logging.DEBUG)

	def __init__(self, currency=None, start_date=None, end_date=None):
		currency = currency if currency else "BRL"
		end_date = end_date if end_date else datetime.now()
		#if current day is in a weekend, the number os days to subtract to get 5 workdays should be greater than 5
		#if current day is saturday it will subtract 6 days, is it's a sunday, it will subtract 7 days
		#this way the default dates when none is given should always be right
		num_day = 5 + (end_date.weekday() - 4 if end_date.weekday() in [5,6] else 0)
		start_date = start_date if start_date else datetime.now() - timedelta(days=num_day)
		
		self.start_date, self.end_date = validate_dates(start_date, end_date)
		self.currency = validate_currency(currency)
		
	def is_valid(self):
		if(self.currency and self.start_date and self.end_date):
			return True
		else:
			return False

	def get_values_from_db(self, date):
		pass

	def get_values_from_api(self, date):
		pass

		