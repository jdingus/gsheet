#!/usr/bin/python
import re
import argparse
import sheetsync
import logging
from creds import USERNAME,PASSWORD,DOCUMENT_KEY
from datetime import datetime,tzinfo
import pytz
from dateutil import tz
from email.utils import parsedate_tz,parsedate
__author__ = 'jdingus'


# logging.getLogger('').setLevel(logging.DEBUG)
logging.basicConfig()

def get_weight():
	""" Return the weight and initialize the argparser
	"""
	parser = argparse.ArgumentParser(description='Script to update google sheet ')
	parser.add_argument('-w','--weight', help='Weight',required=True)
	args = parser.parse_args()

	weight = float(args.weight)	
	print ("Weight entry is: %s" % str(weight))
	print 20*'-'
	return weight

def all_results(source):
	'''
	Returns all results in a google sheet with valid weight entries
	'''
	d =  source.data()
	entries = []

	for k in d:
		weight = d[k]['Weight']
		the_date = d[k]['Date']
		the_date = datetime.strptime(the_date , '%m-%d-%Y')

		if weight:
			weight = float(weight)
			s = (the_date,weight)
			entries.append(s)

	entries.sort()
	results = []
	for item in entries:
		t = item[0].strftime('%m-%d')+' : '+str(item[1])+' lbs'
		# print t
		results.append(t)
	return results


def funct_add_entry(lbs):
	'''
	Enters a given lbs entry into a google sheet as defined by source on current date
	Once entry is given will print out all lb entries currently in sheet
	'''
	username = USERNAME
	password =  PASSWORD
	document_key = DOCUMENT_KEY

	source = sheetsync.Sheet(username=USERNAME,password=PASSWORD,\
							document_key=DOCUMENT_KEY,\
							sheet_name="Weight",\
							key_column_headers=["Date"])	
	
	# take -w arg and current date and add to sheet
	add_entry(source,lbs)
	# get all weights in sheet
	results = all_results(source)
	# print them out
	print_results(results)

def is_datetime_today(datetime_obj):
	'''
	Checks a datetime to see if it shares the same date as now() if so returns True, else return False
	'''
	today=datetime.now()
	to_zone=tz.tzlocal()
	today=today.replace(tzinfo=to_zone)
	if today.date() == datetime_obj.date():
		return True
	else:
		return False

def is_message_weight_entry(message_obj):
	"""
	Parse the body of text to see if it is a weight entry returns entry_bool,date_sent,weight entry
	"""	
	message = message_obj.body
	date_sent = twilio_date_from_message(message_obj.date_sent)
	
	weight_exp = r"([Ww]) ([0-9]{3}[.]*[0-9]{0,1})"
	weight_val = re.search(weight_exp,message)

	if weight_val:
		weight_val = weight_val.group(2)
		return True,date_sent,weight_val
	else:
		return False,0,0

def twilio_date_from_message(date):
	'''
	Takes the date in twillio format and returns in a timezone aware local time
	'''
	date = parsedate_tz(date)
	date = datetime(*(date[0:6]))
	date = date.replace(tzinfo=pytz.UTC)
	date = datetime_to_ltz(date)
	return date

def datetime_to_ltz(date_time):
	''' 
	Convert a datetime which already is tz aware and returns local time zone
	'''
	to_zone = tz.tzlocal()
	local = date_time.astimezone(to_zone)
	return local

def main():
	username = USERNAME
	password =  PASSWORD
	document_key = DOCUMENT_KEY

	source = sheetsync.Sheet(username=USERNAME,password=PASSWORD,\
							document_key=DOCUMENT_KEY,\
							sheet_name="Weight",\
							key_column_headers=["Date"])	
	
	lbs = get_weight()
	
	# take -w arg and current date and add to sheet
	add_entry(source,lbs)

	# get all weights in sheet
	results = all_results(source)	

	# print them out
	print_results(results)

def print_results(results):
	'''
	Prints all of the results
	'''
	for item in results[:-1]:
		print item
	print 20*'-'

def add_entry(source,lbs):
	""" Given a google sheet source and a dict data update the sheet 
		If entry does not exist it will be updated otherwise will be created
		"""
	now = datetime.now()
	date = now.strftime('%m-%d-%Y')
	data = {date: {'Date': date, 'Weight': lbs}}
	source.inject(data)

if __name__ == '__main__':
	main()



