import argparse
import csv
from typing import TYPE_CHECKING

from django.core.management.base import BaseCommand

from books.models import Book

if TYPE_CHECKING:
    from io import TextIOWrapper


class Command(BaseCommand):
    help = 'Populate books Database'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        file_ = options['data_file']  # type: TextIOWrapper
        headers = []
        data = []

        if file_.name.endswith(".csv"):
            reader = csv.reader(file_, delimiter=',')
            for row in reader:
                if not headers:
                    headers = row[:]
                    continue
                row_data = {k: v for k, v in zip(headers, row)}
                data.append(row_data)
                Book.objects.create(**row_data)

        elif file_.name.endswith(".json"):
            self.stdout.write(self.style.WARNING("Coming Soon"))

        self.stdout.write(self.style.SUCCESS('Successfully populated [%d] books' % len(data)))
