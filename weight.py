#!/usr/bin/python
import argparse
import sheetsync
import logging
from creds import USERNAME,PASSWORD,DOCUMENT_KEY
from datetime import datetime
__author__ = 'jdingus'


# logging.getLogger('').setLevel(logging.DEBUG)
logging.basicConfig()

'''
# https://github.com/mbrenig/SheetSync

# Get or create a spreadsheet...
# target = sheetsync.Sheet(username="googledriveuser@domain.com",
#                          password="app-specific-password",
#                          document_name="Let's try out SheetSync")
# # Insert or update rows on the spreadsheet...
# target.inject(data)
# print "Review the new spreadsheet created here: %s" % target.document_href
'''

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
	username = USERNAME
	password =  PASSWORD
	document_key = DOCUMENT_KEY

	source = sheetsync.Sheet(username=USERNAME,password=PASSWORD,\
							document_key=DOCUMENT_KEY,\
							sheet_name="Weight",\
							key_column_headers=["Date"])	
	
	# lbs = get_weight()
	
	# take -w arg and current date and add to sheet
	add_entry(source,lbs)

	# get all weights in sheet
	results = all_results(source)

	# print them out
	print_results(results)

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



