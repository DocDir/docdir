from django.contrib import admin

from .models import Insurer, Plan, Doctor

for model in Insurer, Plan, Doctor:
    admin.site.register(model)
