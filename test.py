import unittest
from CustomerRecords import CustomerRecords


class TestCustomerRecords(unittest.TestCase):
    """Unit tests for the CustomerRecords class"""

    def test_get_distance_method(self):
        """Assert that the distance between hq and the first entry in gistfile1.txt is 41741 meters"""

        test = CustomerRecords('gistfile1.txt', 100000, 53.339428, -6.257664)
        self.assertEqual(test.get_distance(
            53.339428, -6.257664, 52.986375, -6.043701), 41741)

    def test_read_file(self):
        """Assert that there are 16 correct answers in gistfile1.txt"""

        test = CustomerRecords('gistfile1.txt', 100000, 53.339428, -6.257664)
        self.assertEqual(len(test.read_file()), 16)

if __name__ == '__main__':
    unittest.main()