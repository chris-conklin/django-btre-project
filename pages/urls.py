from django.urls import path

from . import views

urlpatterns = [
    # we want the path to point to the root
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
