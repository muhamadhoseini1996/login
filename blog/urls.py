from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('index', views.index, name='blog'),
    path('account-form', views.UserAccount, name='account_form')
]
