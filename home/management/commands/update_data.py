# yourapp/management/commands/update_data.py
from django.core.management.base import BaseCommand
from home.models import *

class Command(BaseCommand):
    help = 'Update data in models to use UTF-8 encoding'

    def handle(self, *args, **options):
        objects = Service.objects.all()
        for obj in objects:
            obj.Description = obj.Description.encode('utf-8')
            obj.save()

        self.stdout.write(self.style.SUCCESS('Data updated successfully.'))
