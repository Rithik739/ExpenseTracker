from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('summary-by-date/', views.summary_by_date, name='summary_by_date'),
    path('summary-by-category/', views.summary_by_category, name='summary_by_category'),
    path('Exit/', views.exit, name='exit'),

]
