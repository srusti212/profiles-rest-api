# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

# APIViews work by defining functions that match the standard Http Methods
class HelloApiView(APIView):
    """ Test API View """

    """ Telling DRF, the serializer we want to use to describe the data that we handle with this API view.
    So right below the dock string above the get function let's add a serializer variable and let's reference our serializer. """

    """                filename/classname"""
    serializer_class = serializers.HelloSerializer

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

    # request contains the data sent through post()
    def post(self, request):
        """ Create a hello message with our name """
        """ This post to APIView returns a message that includes a name that was posted to the API. """
        # Base the serializer on the data that was sent through post() to the API
        serializer = serializers.HelloSerializer(data = request.data)

        """ Checks if the serializer has valid data passed into. """
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object. """
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provided in the request. """
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object. """
        return Response({'method': 'delete'})
