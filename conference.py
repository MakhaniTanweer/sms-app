#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plivo

# Your PLIVO_AUTH_ID and PLIVO_AUTH_TOKEN can be found on your Plivo Dashboard https://manage.plivo.com/dashboard
PLIVO_AUTH_ID = ""
PLIVO_AUTH_TOKEN = ""

# Enter your Plivo phone number. This will show up on your caller ID
plivo_number = "14154290712"

# Enter the URL of where your conferenceXML.py file is
answer_url = "http://198.74.60.200/response/conference/"

# Enter the 3 phone numbers you want to join in on the conference call
# The following format is supported only when bulk calling is enabled: 14155555555<14156666666<14157777777
# Note that this is a delimiter that's specific to Plivo's API, which allows you to call multiple numbers at the same time
# Check out plivo.com/docs/api/call for more info
p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)

conference_numbers = ["13475563967", "13477912649", "13158258178"]
call_params = {
  'from':plivo_number,
  'answer_url':answer_url,
    }

for number in conference_numbers:
  call_params['to'] = number
  print p.make_call(call_params)