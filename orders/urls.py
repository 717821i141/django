from django.urls import path
from . import views

urlpatterns=[
  
    path('b/',views.index2,name='index2'),
     path('c/',views.index3,name='index3'),
]