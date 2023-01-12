from django.test.testcases import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from autographs.models import Person, Address, Letter

from datetime import datetime


class ModelsTestCase(TestCase):

    def setUp(self):
        self.person = Person.objects.create(first_name='Test', last_name="Test")
        self.address = Address.objects.create(
            person=self.person,
            country="Test",
            city='Test',
            zip_code='12-345',
            street='Test',
            number="1/3",
            additional_info="3th floor"
        )

    def test_letter_mark_as_approved(self):
        letter = Letter.objects.create(to_whom=self.person, address=self.address, send_date=timezone.now())

        self.assertFalse(letter.is_responded)
        self.assertIsNone(letter.response_date)

        letter.mark_as_responded()

        self.assertTrue(letter.is_responded)
        self.assertIsNotNone(letter.response_date)

    def test_letter_clean_send_date_later_than_response(self):
        letter = Letter(
            to_whom=self.person,
            address=self.address,
            send_date=datetime.strptime('11-01-2023', '%d-%m-%Y'),
            is_responded=True,
            response_date=datetime.strptime('10-01-2023', '%d-%m-%Y')
        )
        self.assertRaises(ValidationError, letter.save)

    def test_letter_clean_responded_but_not_date(self):
        letter = Letter(
            to_whom=self.person,
            address=self.address,
            send_date=datetime.strptime('11-01-2023', '%d-%m-%Y'),
            is_responded=True,
        )
        self.assertRaises(ValidationError, letter.save)

    def test_letter_clean_not_responded_but_date(self):
        letter = Letter(
            to_whom=self.person,
            address=self.address,
            send_date=datetime.strptime('10-01-2023', '%d-%m-%Y'),
            response_date=datetime.strptime('12-01-2023', '%d-%m-%Y')
        )
        self.assertRaises(ValidationError, letter.save)
