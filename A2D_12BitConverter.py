
def converttoAmps(input_samples):
    valid_samples = [sample for sample in input_samples if sample <= 4094]
    convertsample_to_Amps=[round( 10 * sample/ 4094)for sample in valid_samples]
    return convertsample_to_Amps
    
def Check_InValidSamplesandPrintErrorMessage(input_samples):
    invalid_samples = [sample for sample in input_samples if sample > 4094]
    message="Samples out of range"
    return message
