from django.test import TestCase
from datetime import datetime, timedelta
from .service import ValidationService


class ParametersTests(TestCase):

    # makes sure that the default values are valid
    def test_default_values(self):
        svc = ValidationService()
        self.assertIs(svc.is_valid(), True)

    def test_currency(self):
        svc = ValidationService(currency="EUR")
        self.assertIs(svc.is_valid(), True)
        svc2 = ValidationService(currency="EuR")
        self.assertIs(svc2.is_valid(), True)
        svc3 = ValidationService(currency="eur")
        self.assertIs(svc3.is_valid(), True)
        svc4 = ValidationService(currency="GBP")
        self.assertIs(svc4.is_valid(), False)

    def test_valid_dates(self):
        # five days
        svc = ValidationService(start_date=datetime.strptime(
            "20211122", "%Y%m%d"), end_date=datetime.strptime("20211126", "%Y%m%d"))
        self.assertIs(svc.is_valid(), True)
        # five days, end in weekend
        svc = ValidationService(start_date=datetime.strptime(
            "20211122", "%Y%m%d"), end_date=datetime.strptime("20211127", "%Y%m%d"))
        self.assertIs(svc.is_valid(), True)
        # five days, start in weekend
        svc = ValidationService(start_date=datetime.strptime(
            "20211121", "%Y%m%d"), end_date=datetime.strptime("20211126", "%Y%m%d"))
        self.assertIs(svc.is_valid(), True)
        # five days, weekend in between
        svc = ValidationService(start_date=datetime.strptime(
            "20211119", "%Y%m%d"), end_date=datetime.strptime("20211125", "%Y%m%d"))
        self.assertIs(svc.is_valid(), True)
        # four days, start in weekend
        svc = ValidationService(start_date=datetime.strptime(
            "20211121", "%Y%m%d"), end_date=datetime.strptime("20211125", "%Y%m%d"))
        self.assertIs(svc.is_valid(), True)

    def test_invalid_dates(self):
        # end in the future
        svc = ValidationService(start_date=datetime.now(), end_date=datetime.now() + timedelta(days=6))
        self.assertIs(svc.is_valid(), False)
        # end before start
        svc = ValidationService(start_date=datetime.strptime(
            "20211121", "%Y%m%d"), end_date=datetime.strptime("20211120", "%Y%m%d"))
        self.assertIs(svc.is_valid(), False)
        # more than 5 work days
        svc = ValidationService(start_date=datetime.strptime(
            "20211119", "%Y%m%d"), end_date=datetime.strptime("20211129", "%Y%m%d"))
        self.assertIs(svc.is_valid(), False)
        # less than 5 work days
        svc = ValidationService(start_date=datetime.strptime(
            "20211119", "%Y%m%d"), end_date=datetime.strptime("20211122", "%Y%m%d"))
        self.assertIs(svc.is_valid(), False)
