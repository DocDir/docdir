import datetime

from django.utils import timezone
from django.test import TestCase

from .models import (Doctor, Plan, Specialty, Contact,
                     Contract, DoctorSpecialty, DoctorContact)


class DoctorRelationshipCase(TestCase):
    """
    Abstract base class for testing doctor relationship test cases.
    """
    fixtures = ['simple']

    def assert__intersecting(self, model, **kwargs):
        start = timezone.now()
        end = start + datetime.timedelta(days=30)
        obj_1 = model(start=start, end=end, **kwargs)

        self.assertEqual(len(obj_1._intersecting()), 0,
                         "presave, there should be no intersecting rels")
        obj_1.save()
        self.assertEqual(len(obj_1._intersecting()), 0,
                         "post-save, there should be no intersecting rels")

        assertions = (
            # Intersects end
            ((start + datetime.timedelta(days=15),
              end + datetime.timedelta(days=15)), 1),
            # Intersects start
            ((start - datetime.timedelta(days=15),
              start + datetime.timedelta(days=15)), 1),
            # No intersection (previous)
            ((start - datetime.timedelta(days=15), start), 0),
            # No intersection (after)
            ((end, end + datetime.timedelta(days=5)), 0))

        for (start, end), count in assertions:
            obj_2 = model(start=start, end=end, **kwargs)
            self.assertEqual(len(obj_2._intersecting()), count)


class ContractTest(DoctorRelationshipCase):

    def test__intersecting(self):
        self.assert__intersecting(Contract,
                                  doctor=Doctor.objects.all().first(),
                                  plan=Plan.objects.all().first())
