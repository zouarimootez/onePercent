
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser with default credentials'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
        else:
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))