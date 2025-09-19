
from django.urls import path
from .views import RegistrarContactos

urlpatterns = [
    path('api/contact', RegistrarContactos.as_view()),
]
