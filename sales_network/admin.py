from django.contrib import admin
from django.db.models import QuerySet
from sales_network.models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):

    list_display = ('pk', 'level', 'name', 'email', 'provider_debt')
    list_filter = ('citi',)
    actions = ['set_null',]

    @admin.action(description='Очистить задолженность')
    def set_null(self, request, queryset: QuerySet):
        queryset.update(provider_debt=0)
