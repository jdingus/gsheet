from flask import Flask, request
import my_twilio
app = Flask(__name__)
 
@app.route('/text_entry', methods=['POST'])
def text_entry():
   results = my_twilio.twilio_message()
   return results
 
if __name__ == "__main__":
    app.run(debug=True)