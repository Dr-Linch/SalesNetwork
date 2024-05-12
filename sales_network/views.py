from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from sales_network.models import Provider
from sales_network.serializers import ProviderSerializer, ProviderGetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from sales_network.permissions import IsActive
from rest_framework.serializers import ValidationError


class ProviderViewSet(ModelViewSet):

    queryset = Provider.objects.all()
    default_serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['country',]
    permission_classes = [IsAuthenticated, IsActive]

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'get' or self.action == 'retrieve':
            return ProviderGetSerializer
        else:
            return self.default_serializer_class
