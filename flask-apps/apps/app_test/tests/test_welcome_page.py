from . import BaseTestClass


class TestWelcomePage(BaseTestClass):
    def test_welcome_page_opens(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        