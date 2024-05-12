from rest_framework.serializers import ModelSerializer
from sales_network.models import Provider


class ProviderSerializer(ModelSerializer):

    class Meta:
        model = Provider
        exclude = ('provider_debt',)


class ProviderGetSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'
