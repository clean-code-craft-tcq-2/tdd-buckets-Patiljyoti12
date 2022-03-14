# Test Driven Ranges

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.


## Example

### Input

Consider a set of periodic current samples from a charging session to be:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be in comma-separated (csv format):

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Establish quality parameters: 

- What is the maximum complexity (CCN) per function? 3
- How many lines of duplicate code will you tolerate? 3
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach

1. Write the smallest possible failing test: give input `4,5`. assert output to be `4-5, 2`.
1. Write the minimum amount of code that'll make it pass.
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

#---------------------------------------------------------------------------------------------
Test Specification
 
range_current_measusrements -development source code
test_range_current_measurements-test code

1.rearrange_samples(input_samples)
This method takes charging current samples from one session as input and returns the sorted sequence of samples
Input:
It can be a list with 'n' of elements
Valid Inputs: a) each element in list should be > 0 b) elememts in an list can be consecutive or non-consecutive
Invalid Inputs: a) Empty array b) Negative elements

2.get_ranges_from_samples(input_samples)
This method takes sorted sequence of samples as input and returns all possible ranges from sorted sequence of samples 

3.get_no_of_readings_in_range(samples_ranges)
This method takes range as input and list the total no of occurances of elements in given range 

4. display_samples_details_onconsole(samples_ranges)
This method takes range as input and counts the no of elements within the range and displays the result in csv format 

