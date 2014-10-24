from flask import Flask, request
app = Flask(__name__)
# from site import myapp
# from site import *



from site import mytwilio
 
@app.route('/', methods=['GET'])
def text_entry():
	results = 'stuff'
	results = twilio_message()
	return results
 
if __name__ == "__main__":
    app.run(debug=True)