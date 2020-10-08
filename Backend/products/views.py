from django.shortcuts import render
from rest_framework.views import APIView

class ProductList(APIView):

    def get(self, request):
         