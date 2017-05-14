from rest_framework import serializers
from .models import Debt


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('customer', 'amount', 'status', 'transaction_time')
