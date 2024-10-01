from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Inventory
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

@api_view()     #default accept GET method
def GetItems(request):
    items = Inventory.objects.all()
    serializer = ItemSerializer(items, many=True)
    #return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Item(request, pk):
    item = Inventory.objects.get(pk=pk)
    serializer = ItemSerializer(item)
    #return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)






# class GetItems(APIView):
#     def get(self, request):
#         items = Inventory.objects.all().order_by('-id')
#         serializer = ItemSerializer(items, many=True)
#         #return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)     #json -> complexdata
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class Item(APIView):
#     def get(self, request,pk):
#         item = Inventory.objects.get(pk=pk)
#         serializer = ItemSerializer(item)     #complex datatype->json
#         #return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         snippet = Inventory.objects.get(pk=pk)
#         serializer = ItemSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = Inventory.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# manual json reponse
# def Item(request,pk):
#     item = Inventory.objects.get(pk=pk)
#     data = {'id':item.id,
#             'name':item.name,
#             'category':item.category,
#             'quantity':item.quantity}
#     return JsonResponse(data)