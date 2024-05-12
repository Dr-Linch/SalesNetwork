from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from sales_network.models import Provider
from sales_network.serializers import ProviderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from sales_network.permissions import IsActive


class ProviderViewSet(ModelViewSet):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['country',]
    permission_classes = [IsAuthenticated, IsActive]
