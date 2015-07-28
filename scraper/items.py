# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem

from plans.models import Insurer, Plan


class InsurerItem(DjangoItem):
    """ An ``InsurerItem`` uses the django ``Insurer`` model to back a scrapy
    ``Item``"""
    django_model = Insurer
