# from django.core.management.base import BaseCommand
# from faker import Faker
# from your_app.models import Task

# class Command(BaseCommand):
#     help = "Inserting dummy data for Task model"

#     def __init__(self, *args, **kwargs):
#         super(Command, self).__init__(*args, **kwargs)
#         self.fake = Faker()

#     def add_arguments(self, parser):
#         parser.add_argument(
#             "-n",
#             "--number",
#             nargs=1,
#             type=int,
#             dest="number",
#             required=True,
#             metavar="number",
#         )

#     def handle(self, *args, **options):
#         n = options.get("number")[0]
#         for _ in range(n):
#             Task.objects.create(
#                 title=self.fake.sentence(nb_words=4),
#                 description=self.fake.paragraph(nb_sentences=3),
#                 priority=self.fake.random_int(min=1, max=10),
#                 due_date=self.fake.date_between(start_date="-30d", end_date="+30d"),
#                 completed=self.fake.boolean(chance_of_getting_true=50),
#                 category=self.fake.word(),
#                 tag=self.fake.word(),
#             )


from django.core.management.base import BaseCommand
from faker import Faker
from todolist_app.models import Task

class Command(BaseCommand):
    help = "Insert dummy data for Task model"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            nargs=1,
            type=int,
            dest="number",
            required=True,
            metavar="number",
        )

    def handle(self, *args, **options):
        fake = Faker()
        n = options.get("number")[0]
        for _ in range(n):
            Task.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                priority=fake.random_int(1, 5),
                due_date=fake.date_between(start_date="-1y", end_date="+1y"),
                completed=fake.boolean(),
                category=fake.word(),
                tag=fake.word(),
            )
