from django.db import models

# A magic number for the name CharField max_lengths
NAME_LENGTH = 200

class Insurer(models.Model):
    "An ``Insurer`` is a model for a single health insurer."
    name = models.CharField(max_length=NAME_LENGTH,
                            unique=True,
                            help_text="the name of the insurer")

    def __str__(self):
        return self.name

class Plan(models.Model):
    "A ``Plan`` is a model for a health plan."
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
    "The ``Contact`` model specifies contact information."
    # TODO: max length?
    name = models.CharField(max_length=NAME_LENGTH)
    phone = models.CharField("the phone #",
                             max_length=1,
                             blank=True)
    address = models.TextField("the address")

    # TODO: latlng?

    def __str__(self):
        return self.name or self.phone or self.address


class Doctor(models.Model):
    "A ``Doctor`` is a model for a doctor."
    plans = models.ManyToManyField(Plan,
                                   verbose_name="doctor's plans")
    specialties = models.ManyToManyField(Specialty, through='DoctorSpecialty',
                                         verbose_name="doctor's specialties")
    contacts = models.ManyToManyField(Contact, through='DoctorContact',
                                      verbose_name="doctor's contacts")

    first_name = models.CharField(max_length=NAME_LENGTH)
    last_name  = models.CharField(max_length=NAME_LENGTH)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class DoctorSpecialty(models.Model):
    "``DoctorSpecialty`` is a through model specifying a doctor's specialties."
    specialty = models.ForeignKey(Specialty)
    doctor = models.ForeignKey(Doctor)
    active = models.BooleanField("if the doc's specialty is active",
                                 default=True)

    unique_together = (('doctor', 'contact'))


class DoctorContact(models.Model):
    "A ``DoctorContact`` is a through model connecting a doctor to a contact."
    doctor = models.ForeignKey(Doctor)
    contact = models.ForeignKey(Contact)
    active = models.BooleanField("if the doc's contact is active",
                                 default=True)

    unique_together = (('doctor', 'contact'))
