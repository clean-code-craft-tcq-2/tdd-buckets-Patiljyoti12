import unittest
import range_current_measurements
import A2D_12BitConverter


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
    
    def test_Check_InValidSamplesandPrintErrorMessage(self):
        self.assertTrue(A2D_12BitConverter.Check_InValidSamplesandPrintErrorMessage([4095])=="Samples out of range")
                                                                                    
    def test_converttoAmps(self):
        self.assertTrue(A2D_12BitConverter.converttoAmps([1100, 1802, 3530, 2555, 2000, 3200, 4094]) == [3, 4, 9, 6, 5, 8, 10])
        
    def test_GetSampleRangesFrom_A2D(self):
        self.assertTrue(A2D_12BitConverter.GetSampleRangesFrom_A2D([1100, 1802, 3530, 2555, 2000, 3200, 4094]) == [(3, 6), (8, 10)])
    




if __name__ == '__main__':
  unittest.main()


 
