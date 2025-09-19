from django.urls import path, include

urlpatterns = [
    path('Contactenos/', include('Apps.Catalogos.Contactenos.urls')),
]
