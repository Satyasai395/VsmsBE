from django.urls import path
from . import views

urlpatterns=[
    path('logindata/',views.Index),
    path('logoutuser/',views.logoutuser)
]
