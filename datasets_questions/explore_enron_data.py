#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def prName():
	names = enron_data.keys()
	names.sort()
	for name in names:
		print name

def prPerson(name):
	for l in enron_data[name]:
		print '%25s'%l, ':', enron_data[name][l]

def HowManyPersonInDataset():
	print 'Persons in dataset:', len(enron_data)

def HowManyFeature():
	print 'Features every person:', len(enron_data['PRENTICE JAMES'])

def POITotal():
	cnt = 0
	for person in enron_data:
		if enron_data[person]['poi']:
			cnt += 1
	print 'POI Total in dataset:', cnt

def JamesStock():
	print "Prentice James's stock total value: ",
	print enron_data['PRENTICE JAMES']['total_stock_value']

def ColwellWesleySend2POI():
	print 'Colwell Wesley send email to POI:',
	print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

def JefferyExecrisedStock():
	exercised_stock_options =\
		enron_data['SKILLING JEFFREY K']['exercised_stock_options']
	print 'Skilling Jeffery execrised stock:',
	print exercised_stock_options

def WhoTakeMax():
	lay = enron_data['LAY KENNETH L']['total_payments']
	skilling = enron_data['SKILLING JEFFREY K']['total_payments']
	fastow = enron_data['FASTOW ANDREW S']['total_payments']
	total = lay, skilling, fastow
	totalname = 'Lay (President)', 'Skilling (CEO)', 'Fastow (CFO)'
	m = max(total)
	print totalname[total.index(m)],'take max money:', m

def ValidSalaryOrEmail():
	cnt = 0
	emailcnt = 0
	for person in enron_data:
		if enron_data[person]['salary'] != 'NaN':
			cnt += 1
			# print '%20s'%person, ':', enron_data[person]['salary']
		if enron_data[person]['email_address'] != 'NaN':
			emailcnt += 1
	print 'Valid Salary Persons:', cnt
	print 'Valid Email  Persons:', emailcnt

def HowManyPersonPaymentsNan():
	cntNan = 0
	cntTtl = 0
	for person in enron_data:
		cntTtl += 1
		# print enron_data[person]['total_payments']
		if enron_data[person]['total_payments'] == 'NaN':
			cntNan += 1
	print 'Persons total_payments filled NaN:', 
	print cntNan, ', %.2f%%'%(cntNan*100.0/cntTtl)

def HowManyPOIPaymentsNan():
	cntNan = 0
	cntTtl = 0
	for person in enron_data:
		if not enron_data[person]['poi']:
			continue
		cntTtl += 1
		# print enron_data[person]['total_payments']
		if enron_data[person]['total_payments'] == 'NaN':
			cntNan += 1
	print 'POI total_payments filled NaN:', 
	print cntNan, ', %.2f%%'%(cntNan*100.0/cntTtl)

import sys
sys.path.append("../tools/")
from feature_format import *

HowManyPersonInDataset()
HowManyFeature()
POITotal()
JamesStock()
ColwellWesleySend2POI()
JefferyExecrisedStock()
WhoTakeMax()
ValidSalaryOrEmail()
HowManyPersonPaymentsNan()
HowManyPOIPaymentsNan()

# prPerson('LAY KENNETH L')
# print featureFormat(enron_data, ['total_payments'])