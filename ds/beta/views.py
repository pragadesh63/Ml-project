from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from. import model

class betacls(APIView):
    def post(self):
        value=request.data.get('value')
        model.test(value=value)
        return Response("hi buddy")
