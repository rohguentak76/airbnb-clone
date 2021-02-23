from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import Facility


class Command(BaseCommand):
    help = "this command create Facilities"

    """def add_arguments(self, parser):
        parser.add_argument("--times",
         help="how many times do you want to run command")"""

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for fac in facilities:
            Facility.objects.create(name=fac)
        self.stdout.write(
            self.style.SUCCESS(f"{len(facilities)} Facilities are created!!!")
        )
