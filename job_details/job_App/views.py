from django.shortcuts import render
from .serializer import *
from .models import job_details
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def ListE1(request):
    ListE11 = job_details.objects.all()
    serializers = jobserializers(ListE11,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def postE1(request):
    ListE12 = job_details.objects.all()
    serializer = jobserializers(data=request.data)
    if serializer. is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def putE1(request):
    job_obj = job_details.objects.all(id=id)
    serializer = jobserializers(instance=job_obj,data=request.data)
    if serializer. is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteE1(request,id):
    job_obj = job_details.objects.all(id=id)
    job_obj.delete()
    return Response("job post is deleted")
