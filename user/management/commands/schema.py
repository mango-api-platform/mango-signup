import json
import subprocess

from django.core.management import BaseCommand
from drf_spectacular.generators import SchemaGenerator

from mango_signup.urls import router


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('schema.json', 'w') as f:
            schema = SchemaGenerator(api_version='1.0', patterns=router.urls).get_schema(public=True)
            json.dump(schema, f, indent=2, ensure_ascii=False)
            f.write('\n')

        subprocess.run('npx openapi-typescript@5.4.1 schema.json  -o drf_generated_types.ts', shell=True)
