from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils import timezone

# A magic number for the name CharField max_lengths
NAME_LENGTH = 200

class Insurer(models.Model):
    """An ``Insurer`` is a model for a single health insurer."""
    name = models.CharField(max_length=NAME_LENGTH,
                            unique=True,
                            help_text="the name of the insurer")

    def __str__(self):
        return self.name


class DataSource(models.Model):
    """A ``DataSource`` is a model for where the data was pulled from"""
    SOURCES = (
        ('C', 'Crawled'),
        ('V', 'Official Release csv'),
        ('P', 'Official Release pdf'),
    )

    name = models.CharField(max_length = NAME_LENGTH,
                            verbose_name = "organization name")
    source_type = models.CharField(max_length = 1, choices = SOURCES)
    notes = models.CharField(max_length = NAME_LENGTH,
                             help_text = "assorted notes re: data source")

    unique_together = ('name', 'source_type')

    def __str__(self):
        return "%s, %s" % (self.name, self.source_type)


class Plan(models.Model):
    """A ``Plan`` is a model for a health plan."""
    insurer = models.ForeignKey(Insurer,
                                verbose_name="operating insurer",
                                help_text="the insurer who operates the plan")
    name = models.CharField(max_length=NAME_LENGTH,
                            help_text="the name of the plan")
    # TODO: health plan properties . . .

    def __str__(self):
        return self.name


class Specialty(models.Model):
    """A ``Specialty`` is a category of doctor specialty.

    Family and primary care should be individual categories of specialty.
    """
    name = models.CharField(max_length=NAME_LENGTH)
    description = models.CharField(max_length=NAME_LENGTH)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """The ``Contact`` model specifies contact information."""
    # TODO: max length?
    name = models.CharField(max_length=NAME_LENGTH)
    phone = models.CharField("the phone #",
                             max_length=16,
                             blank=True)
    address = models.TextField("the address", blank=True)

    # TODO: email?
    # TODO: website?
    # TODO: latlng?

    def __str__(self):
        return self.name or self.phone or self.address


class Doctor(models.Model):
    """A ``Doctor`` specifies a doctor's information."""
    plans = models.ManyToManyField(Plan, through='Contract',
                                   verbose_name="doctor's plans")
    specialties = models.ManyToManyField(Specialty, through='DoctorSpecialty',
                                         verbose_name="doctor's specialties")
    contacts = models.ManyToManyField(Contact, through='DoctorContact',
                                      verbose_name="doctor's contacts")

    rip = models.BooleanField(default=False,
                              help_text="whether the doctor is alive")
    first_name = models.CharField(max_length=NAME_LENGTH)
    last_name  = models.CharField(max_length=NAME_LENGTH)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class DoctorRelationship(models.Model):
    """``DoctorRelationship`` is an abstract base class for models connecting a
    relationship a doctor has for a period of time. For example, a doctor might
    have multiple contracts with a single health plan over different periods of
    time.

    These relationship's time periods cannot have overlapping start to end
    ranges.

    Inheriting models must not override the ``start`` or ``end`` fields.
    """
    start = models.DateTimeField(null=True, default=None)
    end = models.DateTimeField(null=True, default=None)
    created = models.DateTimeField(auto_now_add = True,
                                   null = True,
                                   verbose_name = "timestamp record created")
    score = models.FloatField(default = 1.,
                              verbose_name = "data reliability score")
    source = models.ForeignKey(DataSource,
                               null = True,
                               default = None,
                               help_text = "where relationship data comes from")

    def validate_time(self):
        """ Raises valdiation error if end < start"""
        if self.end is not None and self.start is not None and self.end < self.start:
            raise ValidationError({'end': 'Relationship cannot end before it starts.'})

    def validate(self, *args, **kwargs):
        """Template method to be overridden by child class. This further validates the
        model. It should raise a ValidationError if necessary.
        """
        pass

    def save(self, *args, **kwargs):
        """ Overrides ``models.Models.save()`` to include model validation
        If overridden, please be sure to include ``validate_time()``
        """
        self.validate_time()
        self.validate()
        super(DoctorRelationship, self).save(*args, **kwargs)

    def _intersecting(self):
        """Return the ``QuerySet`` of relationships which have overlapping start
        to end ranges.
        """
        if self.end is None:
            return self.__class__.objects.filter(
                start__lt=self.start, end__gt=self.start)
        else:
            return self.__class__.objects.filter(
                Q(start__lt=self.start, end__gt=self.start) |
                Q(start__lt=self.end, end__gt=self.end) |
                Q(start__gt=self.start, end__lt=self.end))

    def active(self):
        """Return whether the relationship is active.

        An active relationship has started in the past, but not ended.
        """
        return self.end is None and self.start < timezone.now()

    class Meta:
        abstract=True


class Contract(DoctorRelationship):
    """A ``Contract`` is a through model specifying a doctor's contracts,
    i.e. the plans the accept.

    Contracts cannot have intersecting start and end dates."""
    doctor = models.ForeignKey(Doctor)
    plan = models.ForeignKey(Plan)


class DoctorSpecialty(DoctorRelationship):
    """``DoctorSpecialty`` is a through model specifying a doctor's
    specialties.

    These doctor specialties cannot have intersecting start and end dates.
    """
    specialty = models.ForeignKey(Specialty)
    doctor = models.ForeignKey(Doctor)


class DoctorContact(DoctorRelationship):
    """A ``DoctorContact`` is a through model specifying a doctor's contacts.

    These doctor contacts cannot have intersecting start and end dates.
    """
    doctor = models.ForeignKey(Doctor)
    contact = models.ForeignKey(Contact)
