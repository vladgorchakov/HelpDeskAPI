from django.test import TestCase
from helpdesk.models import Status


class StatusModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Status.objects.create(title='add status', description='add description')

    def test_title_content(self):
        status = Status.objects.get(id=1)
        expected_object_name = f'{status.title}'
        self.assertEqual(expected_object_name, 'add status')

    def test_description_content(self):
        status = Status.objects.get(id=1)
        expected_object_name = f'{status.description}'
        self.assertEqual(expected_object_name, 'add description')
