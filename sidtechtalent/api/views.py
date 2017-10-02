from rest_framework import viewsets

from django.utils.encoding import force_text
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class Hello(APIView):
    def get(self, request):
        return Response({"hello": "world"})
    

# your ml class here
