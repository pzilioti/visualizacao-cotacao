from datetime import datetime, timedelta
import logging
import sys

logging.basicConfig(format='%(asctime)s %(message)s', stream=sys.stdout, level=logging.DEBUG)


def validate_currency(currency:str):
	if currency.upper() in ["BRL", "EUR", "JPY"]:
		return currency
	else:
		return None

def validate_dates(start_date:datetime, end_date:datetime):
	if(start_date >= end_date):
		logging.warning("Invalid dates - start is equal or greater than end")
		return None, None
	if(end_date > datetime.now()):
		logging.warning("Invalid dates - end is in the future")
		return None, None

	workdays = 0
	#if end date is on a weekend, go back to friday
	if(end_date.weekday() == 6):
		end_date = end_date - timedelta(days=1)
	if(end_date.weekday() == 5):
		end_date = end_date - timedelta(days=1)

	#count how many workdays are beetwen start and end
	aux_date = end_date
	while(aux_date >= start_date):
		if(aux_date.weekday() in [0,1,2,3,4]):
			workdays = workdays + 1
		aux_date = aux_date - timedelta(days=1)

	#too many or to few workdays, invalid dates
	if(workdays > 5 or (workdays <= 4 and start_date.weekday() not in [5,6])):
		logging.warning("Invalid dates")
		return None, None

	#4 days, but start_date is on weekend, we can go back to friday to get one more working day
	if(workdays == 4 and start_date.weekday() in [5,6]):
		logging.warning("Going back to friday")
		num_day = 1 if start_date.weekday() == 5 else 2
		start_date = start_date - timedelta(days=num_day)
	#exactly 5 days
	elif(workdays == 5):
		logging.debug("All good")
		#but start_date is on weekend, let's go to next monday
		if(start_date.weekday() in [5,6]):
			num_day = 2 if start_date.weekday() == 5 else 1
			start_date = start_date + timedelta(days=num_day)

	return start_date, end_date