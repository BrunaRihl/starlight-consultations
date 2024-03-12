from datetime import datetime
import unittest
from unittest.mock import MagicMock, patch
from django.test import RequestFactory
from about.views import about_me


class AboutListViewTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
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
        Test the about_me view function.
        Mocks the behavior of About.objects.all() to return a
        MagicMock object.
        Sends a GET request to the about_me view and checks
        if the response status code is 200.

        """
        mock_about.return_value = MagicMock()

        request = self.request_factory.get("/about")

        response = about_me(request)

        self.assertEqual(response.status_code, 200)
