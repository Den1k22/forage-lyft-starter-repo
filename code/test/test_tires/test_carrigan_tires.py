import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        carriganTires = CarriganTires([0.9, 0, 0, 0])

        self.assertTrue(carriganTires.needs_service())

    def test_tires_should_not_be_serviced(self):
        carriganTires = CarriganTires([0.8, 0.8, 0.8, 0.8])

        self.assertFalse(carriganTires.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)