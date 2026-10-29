"""Tests of the core payment validation behavior."""
import unittest
from payments import validate_amount


class PaymentTests(unittest.TestCase):
    def test_positive_payment_is_allowed(self):
        self.assertTrue(validate_amount(100))

    def test_negative_payment_is_rejected(self):
        self.assertFalse(validate_amount(-10))

    def test_zero_payment_is_rejected(self):
        self.assertFalse(validate_amount(0))


if __name__ == '__main__':
    unittest.main()
