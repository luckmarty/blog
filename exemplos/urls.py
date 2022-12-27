from django.urls import path
from . import views


urlpatterns = [
    path('', views.exemplo01, name="exemplo01"),
]
