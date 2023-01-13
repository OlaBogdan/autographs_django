from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=128, verbose_name=_('First name'))
    last_name = models.CharField(max_length=128, verbose_name=_('Last name'))

    GENDER = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    gender = models.CharField(choices=GENDER, max_length=1, default='M', verbose_name=_('Gender'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    person = models.ForeignKey(Person, related_name='addresses', on_delete=models.CASCADE, verbose_name=_('Person'))
    country = models.CharField(max_length=128, verbose_name=_('Country'))
    city = models.CharField(max_length=128, verbose_name=_('City'))
    zip_code = models.CharField(max_length=128, verbose_name=_('Zip-code'))
    street = models.CharField(max_length=128, verbose_name=_('Street'))
    number = models.CharField(max_length=128, verbose_name=_('Number'))
    additional_info = models.CharField(max_length=256, null=True, verbose_name=_('Additional information'))

    def __str__(self):
        return f'{self.person} ({self.country}, {self.city})'


class Letter(models.Model):
    to_whom = models.ForeignKey(Person, related_name='letters', on_delete=models.PROTECT, verbose_name=_('To whom'))
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name=_('Address'))
    send_date = models.DateField(verbose_name=_('Send date'))
    is_responded = models.BooleanField(default=False, verbose_name=_('Is responded'))
    response_date = models.DateField(blank=True, null=True, verbose_name=_('Response date'))

    def __str__(self):
        return f'{self.address}, {_("send")}: {self.send_date}'

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

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Letter, self).save(*args, **kwargs)
