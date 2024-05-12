from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    actions = ['set_password',]

    @admin.action(description='set_password')
    def set_password(self, request, queriset):
        for obj in list(queriset):
            u = User.objects.get(pk=obj.pk)
            u.set_password(str(obj.password))
            u.save()
            print(u.password)
