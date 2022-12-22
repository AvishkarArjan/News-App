from . import views
from django.urls import path


urlpatterns = [
    path('', views.index , name= 'index'),
    path('indiatoday', views.indiatoday , name='indiatoday'),
    path('nytimes', views.nytimes, name = 'nytimes')
]
