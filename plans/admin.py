from django.contrib import admin

from .models import Insurer, Plan, Doctor, Specialty, Contact

for model in Insurer, Plan, Doctor, Specialty, Contact:
    admin.site.register(model)
