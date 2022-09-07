from rest_framework import serializers
from .models import Budget, Expenses
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()

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

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})
        # Below sets validation restrictions on said password. IE speical chars @!#$
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})
        data['password'] = make_password(password)
        return data
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')