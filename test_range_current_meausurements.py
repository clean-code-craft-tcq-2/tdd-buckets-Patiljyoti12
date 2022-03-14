import unittest
import range_current_measurements


class TypewiseTest(unittest.TestCase):
    def test_Rearrange_Samples(self):
        self.assertTrue(range_current_measurements.rearrange_samples([3, 3, 5, 4, 10, 11, 12]) == [3, 3, 4, 5, 10, 11, 12])
        self.assertTrue(range_current_measurements.rearrange_samples([]) == [])
        
    def test_Display_Samples_Details_onConsole(self):
        self.assertTrue(range_current_measurements.display_samples_details_onconsole([10,11,12]) == '10-12, 3')
    
    def test_get_ranges_from_samples(self):
        self.assertTrue(range_current_measurements.get_ranges_from_samples([3, 3, 5, 4, 10, 11, 12]) == [(3,5),(10,12)])
     
    def test_get_no_of_readings_in_range(self):
        self.assertTrue(range_current_measurements.get_no_of_readings_in_range([10,11,12])==3)


if __name__ == '__main__':
  unittest.main()


 
