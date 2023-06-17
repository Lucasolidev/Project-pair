import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertEqual(result.data, b'{"message":"Hello, World!"}\n')


if __name__ == '__main__':
    unittest.main()
