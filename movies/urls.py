from django.urls import path
from . import views

accounts = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('update-db/', views.update_db, name='update_db'),
]
