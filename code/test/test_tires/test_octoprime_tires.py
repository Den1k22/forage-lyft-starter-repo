import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        octoprimeTires = OctoprimeTires([0.9, 0.9, 0.9, 0.3])

        self.assertTrue(octoprimeTires.needs_service())

    def test_tires_should_not_be_serviced(self):
        octoprimeTires = OctoprimeTires([1, 1, 0.9, 0.0])

        self.assertFalse(octoprimeTires.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)