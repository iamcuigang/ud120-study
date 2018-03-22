#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    datalen = len(ages)
    ### your code goes here
    for i in range(datalen):
        t = (ages[i][0], net_worths[i][0], net_worths[i][0]-predictions[i][0])
        cleaned_data.append(t)
    cleaned_data.sort(lambda x,y:cmp(x[2]*x[2],y[2]*y[2]))
    datalen = datalen*9/10
    cleaned_data = cleaned_data[:datalen]
    # print cleaned_data
    return cleaned_data

