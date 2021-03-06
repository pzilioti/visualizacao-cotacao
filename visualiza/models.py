from django.db import models


class Quotation(models.Model):
    date = models.DateField()
    currency = models.CharField(max_length=3)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'currency'], name='unique_currency_by_date'),
        ]

    def __str__(self):
        return f"{self.currency} : {self.value} in {self.date}"
