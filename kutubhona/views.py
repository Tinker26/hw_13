from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class KitobPageNumberPaginations(PageNumberPagination):
    page_size = 3


class KitobListView(generics.ListCreateAPIView):
    serializer_class = KitobSerializer
    queryset = Kitob.objects.all()
    pagination_class = LimitOffsetPagination

class KitobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KitobSerializer
    queryset = Kitob.objects.all()

class MuallifListView(generics.ListCreateAPIView):
    serializer_class = MuallifSerializer
    queryset = Muallif.objects.all()

class MuallifDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MuallifSerializer
    queryset = Muallif.objects.all()
