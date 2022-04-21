import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for x in phones:
                slugged = slugify(x.get('name'))
                model = Phone(
                    id=x.get('id'),
                    name=x.get('name'),
                    price=int(x.get('price')),
                    image=x.get('image'),
                    release_date=x.get('release_date'),
                    lte_exists=bool(x.get('lte_exists')),
                    slug=slugged
                )
                model.save()
