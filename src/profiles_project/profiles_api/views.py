# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# APIViews work by defining functions that match the standard Http Methods
class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'It is similar to a traditional django view',
        'Gives you the most control over your logic',
        'It is mapped manually to URLs'
        ]

        """ Response object must be passed a dictionary to return a response.
        So the Response object is effectively a dictionary which is converted to json and output to the screen """

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
