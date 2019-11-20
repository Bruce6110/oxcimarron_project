from django.test import SimpleTestCase, TestCase
from .models import Resort


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/skiing/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/skiing/about/')
        self.assertEqual(response.status_code, 200)


class ResortModelTest(TestCase):
    def setUp(self):  # NOTE: This function must be named "setUp(self)"

        Resort.objects.create(resort_name='Cretaceous Heights',
                              location='NM', personal_rating=8.0)
        Resort.objects.create(resort_name='Ice Age Falls',
                              location='NM', personal_rating=9.0)

    def test_text_content(self):

        resort_list = Resort.objects.all()

        for resort in resort_list:
            print("resort:", resort, resort.id)

        # note: if you use the "--keepdb" option with python manage.py test, the id will keep incrementing
        resort = Resort.objects.get(id=2)
        print("ID = ", resort.id)
        print("\n\nRESORT1 = ", resort)
        expected_object_name = f'{resort.resort_name}'
        print(expected_object_name)
        self.assertEqual(expected_object_name, 'just a test')
