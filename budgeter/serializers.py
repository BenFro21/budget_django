from rest_framework import serializers
from .models import Budget, Expenses

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    expenses = serializers.HyperlinkedRelatedField(
        view_name ='expense_detail',
        many = True, 
        read_only = True
    )
    class Meta: 
        model = Budget
        fields =('id', 'title', 'budget_for', 'income', 'total', 'expenses')
        
class ExpensesSerializer(serializers.HyperlinkedModelSerializer):
    budget = serializers.HyperlinkedRelatedField(
        view_name = 'budget_detail',
        read_only = True
    )
    class Meta:
        model = Expenses
        fields =('id', 'budget', 'title', 'biller', 'amount_planned', 'amount_actual', 'type_bill')