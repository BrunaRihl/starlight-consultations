# Create your tests here.
import unittest
from unittest.mock import MagicMock, patch
from django.test import RequestFactory
from about.views import about_me
from datetime import datetime 


class AboutListViewTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by initializing common resources.
        """
        self.request_factory = RequestFactory()
        self.mocked_about = [
            {
            "id": 1,
            "title": "About",
            "updated_on": datetime(2022, 12, 28, 23, 55, 59, 342380),
            "content": "loren ipsun",
        }
        ]
        

    @patch("about.views.About.objects.all")
    def test_about_me_view(self, mock_about):
        """
        Test case for the about_me view.
        """
        mock_about.return_value = MagicMock()
        
        request = self.request_factory.get("/about")

        response = about_me(request)

        self.assertEqual(response.status_code, 200)
