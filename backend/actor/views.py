from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from actor.models import Person
from actor.serializers import partSerializer


@api_view(['GET', 'POST'])
def allnumber(request, format=None):
    if request.method == 'GET':
        numbers = Person.objects.all()
        serializer = partSerializer(numbers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        numbers = partSerializer(data=request.data)
        if numbers.is_valid():
            numbers.save()
            return Response(numbers.data, status=status.HTTP_201_CREATED)
        return Response(numbers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def number(request, pk, format=None):

    try:
        one = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = partSerializer(one)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = partSerializer(one, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
