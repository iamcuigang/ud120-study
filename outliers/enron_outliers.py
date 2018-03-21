#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop('TOTAL', 0)

if False: ########## Find Outliers' Name
	sortdata = []
	for p in data_dict:
		if data_dict[p]['salary'] == 'NaN' or data_dict[p]['bonus'] == 'NaN':
			continue
		sortdata.append( (p, data_dict[p]['salary'], data_dict[p]['bonus']) )
	sortdata.sort(lambda x,y : cmp(x[1], y[1]))
	print sortdata[-4:]
	sortdata.sort(lambda x,y : cmp(x[2], y[2]))
	print sortdata[-4:]

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


