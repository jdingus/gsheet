import re
import weight
from creds import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

def main():

    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    messages = client.messages.list()
    for item in messages:
        response = weight.is_message_weight_entry(item)
        if response[0]:
            print response

if __name__ == '__main__':
    main()



"""
    weight_val = re.search(weight_exp,body_text)
    date_sent = item.date_sent

    if weight_val:
        print date_sent,' : ',weight_val.group(2)

raise SystemExit

# A list of message objects with the properties described above
messages = client.messages.list()
for item in messages:
    body_text = item.body
    weight_val = re.search(weight_exp,body_text)
    date_sent = item.date_sent

    if weight_val:
        print date_sent,' : ',weight_val.group(2)
""" 


"""
>gweight<

Send a text to a twillio number.  This causes a url hit to my app which then parses the given text
and if is a 'weight entry' will execute my python function which add it to my google sheet.
Another function of the app is to send me daily/weekly updates, encouraging me and gaging my progress.

>> Overview of Steps Needed [Backwards] <<

-1.) (100%) weight.funct_add_entry(date_entry,lbs) # Take weight entry and add to google sheet

-996.) if entry_bool==False  > Exit
        
        if entry_bool==True
            (date_entry,lbs) = parse_weight_date(message)

-997.) (entry_bool,date,message) = is_message_weight_entry(message) Parse the body of text to see if it is a weight entry returns entry_bool,message
-998.) www.gweight.com/<USER>/weight-entry/<UNIQUE ID> Custom url is triggered upon receipt of a text message
-999.) Text is sent to a twillio number 'w 234.5' "
"""