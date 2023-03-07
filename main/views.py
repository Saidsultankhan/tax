from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Company
from main.serializers import CompanySerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_company(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


class CompanyUpdate(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# class CompanyAPIView(APIView):
#     def get(self, request):
#         company = Company.objects.all()
#         return Response({'companies': CompanySerializer(company, many=True).data})
#
#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         serializer.is_valid(raise_exeption=True)
#         serializer.save()
#         return Response({'company': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Company.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = CompanySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exeption=True)
#         serializer.save()
#         return Response({'company': serializer.data})