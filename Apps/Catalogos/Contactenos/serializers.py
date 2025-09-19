from rest_framework.serializers import ModelSerializer
from .models import Contactos

class ContactosSerializer(ModelSerializer):
    class Meta:
        model = Contactos
        fields = '__all__'