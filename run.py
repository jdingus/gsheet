# import os
from site import app

# def runserver():
# 	port = int(os.environ.get('PORT', 5000))
# 	app.run(host='0.0.0.0', port=port)
"""
@app.route('/', methods=['GET'])
def text_entry():
	results = 'stuff'
	results = twilio_message()
	return results

if __name__ == "__main__":
    app.run(debug=True)
   """

def runserver():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	runserver()