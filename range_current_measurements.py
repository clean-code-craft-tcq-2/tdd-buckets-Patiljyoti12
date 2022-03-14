import numpy as np

#sort the given input sequence
def rearrange_samples(input_samples):
    input_samples.sort()
    return input_samples
    
#get the ranges from the given input sequence
def get_ranges_from_samples(input_samples):
    myarray =Rearrange_Samples(input_samples)
    sequences = np.split(myarray, np.array(np.where(np.diff(myarray) > 1)[0]) + 1)
    samples_ranges = []
    for s in sequences:
        if len(s) > 1:
            samples_ranges.append((np.min(s), np.max(s)))
        else:
            samples_ranges.append(s[0])
    print(samples_ranges)
    return samples_ranges
   

#get the no of readings in given range
def get_no_of_readings_in_range(samples_ranges):
    result=len(list(x for x in samples_ranges if samples_ranges[0] <= x <=samples_ranges[-1] ))
    return result

#to display the ranges and no of occurences 
def display_samples_details_onconsole(samples_ranges):
    count=get_no_of_readings_in_range(samples_ranges)
    message= (f"{samples_ranges[0]}-{samples_ranges[-1]}, {count}")
    return message
  

