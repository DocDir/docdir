import datetime

from django.utils import timezone
from django.test import TestCase

from .models import (Doctor, Plan, Specialty, Contact,
                     Contract, DoctorSpecialty, DoctorContact)


class DoctorRelationshipCase(TestCase):
    """Abstract base class for testing doctor relationship test cases.
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
            # Intersects interior
            ((start + datetime.timedelta(days=5),
              start + datetime.timedelta(days=25)), 1),
            # Intersects entire
            ((start - datetime.timedelta(days=5),
              end + datetime.timedelta(days=5)), 1),
            # No intersection (previous)
            ((start - datetime.timedelta(days=15), start), 0),
            # No intersection (after)
            ((end, end + datetime.timedelta(days=5)), 0),
            # Start only, intersects
            ((start + datetime.timedelta(days=15), None), 1))

        for (start, end), count in assertions:
            obj_2 = model(start=start, end=end, **kwargs)
            self.assertEqual(len(obj_2._intersecting()), count)

    def assert_active(self, model, **defaults):
        now = timezone.now()

        obj = model(start=now + datetime.timedelta(days=1), **defaults)
        self.assertFalse(obj.active(),
                         "a rel which starts in the future isn't active")

        obj = model(end=now - datetime.timedelta(days=1),
                    **defaults)
        self.assertFalse(obj.active(),
                         "a rel with an end isn't active")

        obj = model(start=now + datetime.timedelta(days=1),
                    end=now + datetime.timedelta(days=2),
                    **defaults)
        self.assertFalse(obj.active(),
                         "a rel with an end + in the future isn't active")

        obj = model(start=now - datetime.timedelta(days=1), **defaults)
        self.assertTrue(obj.active(),
                        "a rel with a start in the past and no end is active")


class ContractTest(DoctorRelationshipCase):

    def _defaults():
        return {'doctor': Doctor.objects.all().first(),
                'plan': Plan.objects.all().first()}

    def test__intersecting(self):
        self.assert__intersecting(Contract, **ContractTest._defaults())

    def test_active(self):
        self.assert_active(Contract, **ContractTest._defaults())


class DoctorSpecialtyTest(DoctorRelationshipCase):

    def _defaults():
        return {'doctor': Doctor.objects.all().first(),
                'specialty': Specialty.objects.all().first()}

    def test__intersecting(self):
        self.assert__intersecting(DoctorSpecialty,
                                  **DoctorSpecialtyTest._defaults())

    def test_active(self):
        self.assert_active(DoctorSpecialty, **DoctorSpecialtyTest._defaults())


class DoctorContactTest(DoctorRelationshipCase):

    def _defaults():
        return {'doctor': Doctor.objects.all().first(),
                'contact': Contact.objects.all().first()}

    def test__intersecting(self):
        self.assert__intersecting(DoctorContact,
                                  **DoctorContactTest._defaults())

    def test_active(self):
        self.assert_active(DoctorContact, **DoctorContactTest._defaults())
