from users.models import User
from django.core import management


class Command(management.BaseCommand):

    def handle(self, *args, **options):

        u = User.objects.create(email='just_email@mail.ru', active=True, is_superuser=True, is_staff=True)
        u.set_password('just_pass')
        u.save()
