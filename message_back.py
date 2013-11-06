#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, Response, request
import simplejson as json
import plivoxml
import plivo

PLIVO_AUTH_ID = "MANTLJODIXMTJKNJDMYJ"
PLIVO_AUTH_TOKEN = "MWY5MzIxNjAyYWUzOTc1MjZjMDViNDYxNTAwYTFh"
plivo_number = "14154290712"
data = []

app = Flask(__name__)

@app.route('/response/message_back/', methods=['GET', 'POST'])
def message_back():
    if request.method == 'POST':
        print request.form
        from_num = request.form.get('From')
        from_parameters = request.form.get('Text')
        from_parameters = from_parameters.strip().split()
        print from_parameters

        person = {}
        person['phone_num'] = long(from_num)
        person['country_code'] = from_parameters[0]
        person['pregancy_stage'] = int(from_parameters[1])
        person['has_smartphone'] = False 
        person['language'] = 'english'
        person['responsiveness'] = 5
        
        add_person(person)
        
        subscriber_msg = "You are now subscribed to the feed"
        message_params = {
            'src':plivo_number,
            'dst':from_num,
            'text':subscriber_msg,
        }
        p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)
        res = p.send_message(message_params)
        return str(res)
        
        
@app.route('/subscribers/', methods=['GET'])
def get_subscriber():
    global data
    read_data()
    country_code = request.args.get('country_code')
    if country_code == None:
        return Response( json.dumps(data),  mimetype="application/json")     
    else:
        return_data = filter(lambda x: x['country_code'] == country_code, data)
        return Response( json.dumps(return_data),  mimetype="application/json")     
        
def save_data():
    global data
    with open('subscribers.txt', 'w') as fp:
        json.dump(data, fp)
        
def read_data():
    global data
    with open("subscribers.txt", 'r') as fp:
        data = json.load(fp)  

def add_person(person_dict):
    print person_dict
    global data
    read_data()
    data.append(person_dict)
    save_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)