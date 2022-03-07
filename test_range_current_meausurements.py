import unittest
import range_current_measurements


class TypewiseTest(unittest.TestCase):
    def test_no_of_readings_in_range(self):
        self.assertTrue(range_current_measurements.get_no_of_readings_in_range([3,3,4,5],4,5) == 2)
        
    def test_no_readings_in range(self):
         self.assertTrue(range_current_measurements.get_no_of_readings_in_range([3,3,4,5,7,9],-1,-2) == 0)


if __name__ == '__main__':
  unittest.main()


 
