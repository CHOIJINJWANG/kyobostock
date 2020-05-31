from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:isbn>/', views.result, name='result'),
    path('select/', views.select, name='select'),
    path('login/', views.login, name='login'),

]