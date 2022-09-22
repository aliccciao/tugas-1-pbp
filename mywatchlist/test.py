from django.test import TestCase, Client
from django.urls import reverse

class MyWatchListResponseTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_html_exists(self):
        response = self.client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEqual(response.status_code, 200)
    
    def test_url_json_exists(self):
        response = self.client.get(reverse("mywatchlist:show_json"))
        self.assertEqual(response.status_code, 200)

    def test_url_xml_exists(self):
        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)

    def test_url_json_by_id_exists(self):
        response = self.client.get(reverse("mywatchlist:show_json_by_id"))
        self.assertEqual(response.status_code, 200)

    def test_url_xml_by_id_exists(self):
        response = self.client.get(reverse("mywatchlist:show_xml_by_id"))
        self.assertEqual(response.status_code, 200)