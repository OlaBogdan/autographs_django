from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    GENDER = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    gender = models.CharField(choices=GENDER, max_length=1, default='M')


class Address(models.Model):
    person = models.ForeignKey(Person, related_name='addresses', on_delete=models.CASCADE)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    additional_info = models.CharField(max_length=256)


class Letter(models.Model):
    to_whom = models.ForeignKey(Person, related_name='letters', on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    send_date = models.DateField()
    is_responded = models.BooleanField(default=False)
    response_date = models.DateField(blank=True)

    def mark_as_responded(self):
        self.is_responded = True
        self.response_date = timezone.now()
        self.save()

    def clean(self):
        if self.response_date and self.send_date > self.response_date:
            raise ValidationError(_('Send date cannot be late than response date!'))

        if self.is_responded and not self.response_date:
            raise ValidationError(_('Response date is unfilled!'))

        if self.response_date and not self.is_responded:
            raise ValidationError(_('Letter is not set as responded!'))
