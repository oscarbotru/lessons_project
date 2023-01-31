from django.core.management import BaseCommand

from funny.models import Student
from funny.services import send_emails


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_emails()
