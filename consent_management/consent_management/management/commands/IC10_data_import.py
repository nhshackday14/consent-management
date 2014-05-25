from django.core.management.base import BaseCommand
from consent_management.models import Procedure


DEFAULT_PROCEDURE_FILE = "../ICT_data/procedures.txt"


def parse_row(row):
    fields = row.split(" ", 1)
    return Procedure(name=fields[1])


def read_file(fname=DEFAULT_PROCEDURE_FILE):
    with open(fname) as f:
        for line in f:
            row = parse_row(line)
            row.save()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if len(args):
            read_file(args[0])
        else:
            read_file()
