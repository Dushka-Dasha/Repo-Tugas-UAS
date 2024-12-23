import unittest
from basic.euclidian import Euclid

class TestEuclid(unittest.TestCase):
    def setUp(self):
        self.euclid = Euclid()

    def test_gcd_positive(self):
        self.assertEqual(self.euclid.gcd(48, 18), 6)
        self.assertEqual(self.euclid.gcd(101, 103), 1)

    def test_gcd_negative(self):
        self.assertEqual(self.euclid.gcd(-48, 18), 6)
        self.assertEqual(self.euclid.gcd(48, -18), 6)

    def test_gcd_zero(self):
        self.assertEqual(self.euclid.gcd(0, 18), 18)
        self.assertEqual(self.euclid.gcd(18, 0), 18)

    def test_gcd_both_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.euclid.gcd(0, 0)

if __name__ == "__main__":
    unittest.main()
