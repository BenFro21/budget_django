from django.urls import path 
from . import views

urlpatterns =[
    path('budgets/', views.BudgetList.as_view(), name='budget_list'),
    path('budgets/<int:pk>/', views.BudgetDetail.as_view(), name='budget_detail'),
    path('expenses/', views.ExpensesList.as_view(), name='expense_list'),
    path('expenses/<int:pk>/', views.ExpensesDetail.as_view(), name='expense_detail')
]