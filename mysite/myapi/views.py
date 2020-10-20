from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import HealthSerializer
from rest_framework import status
from .models import Health

class HealthListView (APIView):
    def get (self, request):
        Healths = Health.objects.all()
        serializer = HealthSerializer(Healths, many=True)
        return Response(serializer.data)
    def post(self, request):

        serializer= HealthSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)