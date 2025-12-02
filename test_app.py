import unittest
from app import flaskAppInstance

class TestCloudOpsApp(unittest.TestCase):

    def setUp(self):
        # Set up a test client for our Flask app
        self.app = flaskAppInstance.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        # Test 1: Check if the home page returns code 200 (OK)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if our title is present in the HTML
        self.assertIn(b"CloudOps Resource Manager", response.data)

    def test_add_server(self):
        # Test 2: Simulate adding a new server via POST request
        response = self.app.post('/add', data=dict(
            name="Unit-Test-Server",
            ip="10.0.0.99",
            status="Maintenance"
        ), follow_redirects=True)
        
        # Check if the response is OK and the new server appears in the list
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Unit-Test-Server", response.data)
        self.assertIn(b"10.0.0.99", response.data)

if __name__ == "__main__":
    unittest.main()
