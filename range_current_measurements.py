#Function to get no of readings in given range
def get_no_of_readings_in_range(input_samples,start_range,stop_range):
  count=0
  for x in input_samples:
    if x>=start_range and x<=stop_range:
      count=count+1
  return count
