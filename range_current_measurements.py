#Function to get no of readings in given range
def get_no_of_readings_in_range(input_samples,start_range,stop_range):
  result=len(list(x for x in input_samples if start_range <= x <= stop_range))
  return result
