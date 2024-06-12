from .models import Locomotive  
from .serializers import LocomotivesSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def locomotive_list(request, format=None):

    if request.method == 'GET':
        locos = Locomotive.objects.all()
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def locomotive_details(request,name, format=None):
    try:
        locomotive = Locomotive.objects.get(pk=name.upper())
    except Locomotive.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LocomotivesSerializer(locomotive)
        if locomotive.motive_power=="Electric":
            serializer.electric_filter()
        elif(locomotive.motive_power == "Diesel" and locomotive.gauge == "Broad"):
            serializer.broadDiesel_filter()
        elif(locomotive.motive_power == "Electric/Diesel" or (locomotive.motive_power == "Diesel" and locomotive.gauge != "Broad")):
            serializer.standard_filter()
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LocomotivesSerializer(locomotive, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        locomotive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def electric_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(motive_power = "Electric")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def diesel_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(motive_power = "Diesel")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def broad_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(gauge = "Broad")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def meter_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(gauge = "Meter")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def narrow_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(gauge = "Narrow")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def narrower_list(request, format=None):
    if request.method == 'GET':
        locos = Locomotive.objects.all().filter(gauge = "Narrower")
        serializer = LocomotivesSerializer(locos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LocomotivesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)