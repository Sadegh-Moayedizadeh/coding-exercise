from django.test import Client, TestCase

# Create your tests here.

class SampleTest(TestCase):
    def setUp(self):
        self.cli = Client()

    def test(self):
        response = self.cli.get('/postal_card/?text={text}'.format(text='سلام۲دنیا2'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('سلام۲دنیا۲' in response.content.decode('utf-8'))
