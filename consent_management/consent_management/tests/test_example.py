from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexTestCase(TestCase):
    url = reverse('index')

    def test_get_200(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
