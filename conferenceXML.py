from flask import Flask, Response
import plivoxml

app=Flask(__name__)

@app.route('/response/conference/', methods=['GET'])
def conference():
    response = plivoxml.Response()
    response.addSpeak('Hello. This is intel code fest. Please eat lots of pizza')
    
    conference_name = "demo"
    response.addConference(conference_name)

    return Response(str(response), mimetype='text/xml')
    
@app.route('/')
def index():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')