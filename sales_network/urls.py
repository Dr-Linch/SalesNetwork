from django.urls import path
from sales_network.apps import SalesNetworkConfig
from sales_network.views import ProviderViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('provider', ProviderViewSet)

app_name = SalesNetworkConfig.name

urlpatterns = [

] + router.urls
