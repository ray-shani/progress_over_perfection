# /home/rayshani/Django_practices/saturday_project/book_store/urls.py

from django.urls import path
from . import views

app_name = 'book_store' # This line is important

urlpatterns = [
    path('', views.index, name='index'),
]