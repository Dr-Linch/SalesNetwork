from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales_network.urls', namespace='sales')),
    path('login/', include('users.urls', namespace='login')),
]
