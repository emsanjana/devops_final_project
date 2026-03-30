import unittest
import json
from app.app import app

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n Starting Flask App Test...\n")

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    # Test Case 1: Home Route
    def test_home_route(self):
        response = self.client.get('/')
        try:
            self.assertEqual(response.status_code, 200)
            print("PASS: Home route is accessible (Status 200)")
        except AssertionError:
            print("FAIL: Home route failed")
            raise

    # Test Case 2: Invalid Route (404)
    def test_invalid_route(self):
        response = self.client.get('/invalid')
        try:
            self.assertEqual(response.status_code, 404)
            print("PASS: Invalid route returns 404")
        except AssertionError:
            print("FAIL: Invalid route did not return 404")
            raise

    # Test Case 3: Content Check
    def test_home_content(self):
        response = self.client.get('/')
        try:
            self.assertIn(b"Database", response.data)
            print("PASS: Expected content found in response")
        except AssertionError:
            print("FAIL: Expected content NOT found")
            raise

    # Test Case 4: Response Time Check (basic)
    def test_response_time(self):
        import time
        start = time.time()
        self.client.get('/')
        end = time.time()

        try:
            self.assertLess(end - start, 1)  # must respond within 1 sec
            print("PASS: Response time is under 1 second")
        except AssertionError:
            print("FAIL: Response too slow")
            raise

    # Test Case 5: Headers Check
    def test_headers(self):
        response = self.client.get('/')
        try:
            self.assertIn('Content-Type', response.headers)
            print("PASS: Response headers are correct")
        except AssertionError:
            print("FAIL: Headers missing")
            raise

    # Test Case 6: Method Not Allowed
    def test_method_not_allowed(self):
        response = self.client.post('/')
        try:
            self.assertIn(response.status_code, [200, 405])
            print("PASS: Method handling is correct")
        except AssertionError:
            print("FAIL: Unexpected method behavior")
            raise

    @classmethod
    def tearDownClass(cls):
        print("\nTest Suite Completed!\n")

if __name__ == '__main__':
    print("\nStarting Flask App Test...\n")

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FlaskAppTest)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    passed = total - failed

    print("\n Test Summary:")
    print(f"Total Tests   : {total}")
    print(f"Passed        : {passed}")
    print(f"Failed        : {failed}")

    if failed == 0:
        print("\nALL TESTS PASSED SUCCESSFULLY!\n")
    else:
        print("\nSOME TESTS FAILED!\n")
