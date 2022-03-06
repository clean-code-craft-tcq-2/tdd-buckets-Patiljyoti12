import range_current_measurements


def test_no_of_readings_in_range(input_samples,start_range,stop_range,expected_result):
  result=range_current_measurements.get_no_of_readings_in_range(input_samples,start_range,stop_range)
  assert result==expected_result
  
if __name__ == '__main__':
  #Testcase1
  start_range=4
  stop_range=5
  input_samples=[3,3,5,4]
  test_no_of_readings_in_range(input_samples,start_range,stop_range,expected_result)

  
  
