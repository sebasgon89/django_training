from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:username>', views.hello),
    path('about/', views.about),
]