import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','atividade3.settings')

import django
django.setup()

import random
from mtv.models import Topic,Page,Access
from faker import Faker

fakegen = Faker()

for i in range(10):
    t=Topic.objects.get_or_create(name="Roger Rogerio")[0]

    p=Page.objects.get_or_create(topic =t,
                                name = fakegen.name,)[0]
    a=Access.objects.get_or_create(page =p,
                               created_at= fakegen.date())[0]