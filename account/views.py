from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):   #perform_create
            serializer.save()
            return Response('Successfully registered on StackOverFlow14!', status=201)

