import re
import weight
from creds import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

def twilio_message():
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    entries_today=[]

    messages = client.messages.list()
    for item in messages:
        response = weight.is_message_weight_entry(item)
        # If response is True
        if response[0]:
            # If entry is same date as now()
            if weight.is_datetime_today(response[1]):
                entries_today.append(response)
    # On last entry for the day enter it into google sheet
    if entries_today:
        last_lb_entry = entries_today[0][-1]
        results = weight.funct_add_entry(last_lb_entry)
        return results


def main():

    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    entries_today=[]

    messages = client.messages.list()
    for item in messages:
        response = weight.is_message_weight_entry(item)
        # If response is True
        if response[0]:
            # If entry is same date as now()
        	if weight.is_datetime_today(response[1]):
	        	entries_today.append(response)
    # On last entry for the day enter it into google sheet
    if entries_today:
        last_lb_entry = entries_today[0][-1]
        weight.funct_add_entry(last_lb_entry)


if __name__ == '__main__':
    main()