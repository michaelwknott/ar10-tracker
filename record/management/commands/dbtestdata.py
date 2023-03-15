import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from record.models import CompetitionData, CustomUser, TrainingData


class Command(BaseCommand):
    help = "Adds test data to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "num_records",
            type=int,
            help="Indicates the number of test records to add to the database",
        )

    def handle(self, *args, **kwargs):
        num_records = kwargs["num_records"]
        fake = Faker()

        competition_list = [
            "ESSU",
            "British Championships",
            "Intershoot",
            "ISSf World Cup 1",
            "ISSf World Cup 2",
            "ISSf World Cup 3",
            "ISSf World Cup 4",
            "BPC",
            "RIAC",
            "BOAG",
            "European Games",
            "Olympic Games",
        ]

        username = CustomUser.objects.get()

        for _ in range(num_records):
            training_record = TrainingData.objects.create(
                user=username,
                date=fake.date_between(start_date="-1y", end_date="now"),
                number_shots=60,
                score=random.uniform(600.0, 630.1),
                target_distance=10,
                f_coefficient=fake.random_int(min=0, max=10, step=1),
                aiming_time=random.uniform(5.1, 19.9),
                ten_zero=fake.random_int(min=80, max=99, step=1),
                ten_azero=fake.random_int(min=80, max=99, step=1),
                ten_five=fake.random_int(min=80, max=99, step=1),
                ten_afive=fake.random_int(min=80, max=99, step=1),
                s1=random.uniform(5.0, 16.9),
                s2=random.uniform(5.0, 16.9),
                da=random.uniform(3.0, 12.9),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"{training_record}: Successfully added to the database."
                )
            )

        for _ in range(num_records):
            competition_record = CompetitionData.objects.create(
                user=username,
                competition_name=random.choice(competition_list),
                date=fake.date_between(start_date="-1y", end_date="now"),
                match_number=fake.random_int(min=1, max=3, step=1),
                qual_score=random.uniform(600.0, 630.1),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"{competition_record}: Successfully added to the database."
                )
            )
