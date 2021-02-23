from django.core.management.base import BaseCommand

# from rooms import models as room_models
from rooms.models import HouseRule


class Command(BaseCommand):
    help = "this command create rules"

    """def add_arguments(self, parser):
        parser.add_argument("--times",
         help="how many times do you want to run command")"""

    def handle(self, *args, **options):
        rules = [
            "animal available",
            "smoking available",
            "animal unavailable",
            "No smoking",
        ]
        for r in rules:
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(rules)} rules are created!!!"))
