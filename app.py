from flask import Flask, request
app = Flask(__name__)

import my_twilio
 
@app.route('/', methods=['GET'])
def text_entry():
	results = 'stuff'
	# results = my_twilio.twilio_message()
	return results
 
if __name__ == "__main__":
    app.run(debug=True)