from .models import Locomotive  
from .serializers import LocomotivesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
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
def locomotive_details(request,name, format=None):
    try:
        locomotive = Locomotive.objects.get(pk=name.upper())
    except Locomotive.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LocomotivesSerializer(locomotive)
        if locomotive.motive_power=="Electric" and locomotive.gauge == "Broad":
            serializer.broad_electric()
        elif(False):
            pass
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