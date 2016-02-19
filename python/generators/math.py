def average(generator):
    """
    Send a generator which has int values all over and 
    return average of those values. 

    TODO : convert this into reduce statement
    TODO2 : Make this moving average for streaming values, updates the average 
    when generator gets a new value
    """
    s = 0
    n = 0
    for val in generator:
        n+=1
        s+=val
    return s*1.0/n

def standard_deviation(generator):
    """
    given a generator of integer values
    returns its standard deviation
    """
    
