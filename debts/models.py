from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

"""
    Importing the Customer Model from the Profiles app.
    One user may have several debts/transactions, but only one transaction can be owned by that one User.
    Use ForeignKey field.

            """

from profiles.models import Customer


# This function serves to validate that a Negative Loan value cannot be stored in DB
def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is Negative. One cannot be allocated a Negative Amount'),
            params={'value': value},
        )


class Debt(models.Model):  # This is the Debt model
    PAID = 'Paid'
    PAYING = 'Paying'
    DEFAULTER = 'Defaulter'

    """
        These are the possible allowed values for a loan status. A customer could :
                1. Have finished paying the debt/loan (Cleared)
                2. Be paying the debt (In Progress)
                3. Have Defaulted from paying the loan
    """
    LOAN_STATUSES = (
                    (PAID, 'Paid'),
                    (PAYING, 'Paying'),
                    (DEFAULTER, 'Defaulter'))

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=LOAN_STATUSES, default=PAYING)
    amount = models.DecimalField(blank=False, max_digits=9, decimal_places=2, default=0, validators=[validate_positive])
    transaction_time = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return("Loan Status for {} {}".format(self.customer.first_name, self.customer.last_name))

    class Meta:
        db_table = 'tbl_due_listin'
        managed = True
