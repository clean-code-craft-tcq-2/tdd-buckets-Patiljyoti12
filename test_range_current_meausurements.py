import range_current_measurements

start_range=3
stop_range=6
input_sample=1,2,6,7,8
expected_result=2

def test_no_of_readings_in_range(input_samples,start_range,stop_range,expected_result):
  result=get_no_of_readings_in_range(input_samples,start_range,stop_range)
  assert result==expected_result
  
if __name__ == '__main__':
   test_no_of_readings_in_range(input_samples,start_range,stop_range,expected_result)

  
  
