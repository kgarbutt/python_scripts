
#! /usr/bin/env python3

import os
import requests
# import json

# Path to corpweb directory
path = "/data/feedback/"

# Returns list of all files & directories
text_files = os.listdir( path )

# corpweb-external-IP
url = 'http://34.67.216.97/feedback/'

# Dictionary with keys & values for feedback content
feedback_dict = {}
keys = ['title' ,'name' ,'date' ,'feedback']


for file in text_files:
	with open(path + file) as feedback:
		i = 0
		for line in feedback:
			feedback_dict[keys[i]] = line.rstrip('\n')
			i += 1
		response = requests.post(url, data = feedback_dict)
		print("status_code "+ str(response.status_code))


