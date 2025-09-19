from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
from rest_framework.views import APIView
import logging.handlers

from Apps.Catalogos.Contactenos.models import Contactos
from Apps.Catalogos.Contactenos.serializers import ContactosSerializer

logger = logging.getLogger(__name__)

class RegistrarContactos(APIView):

    @swagger_auto_schema(request_body=ContactosSerializer, responses={201: ContactosSerializer(many=True)})
    def post(self, request):
        """Ingresar el contacto
        """
        logger.info('POST request to list all Contacts')
        serializer = ContactosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info('Contact created successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('Failed to contact: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)