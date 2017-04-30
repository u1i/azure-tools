# Takes a filename from the local filesystem, then uses
# Azure Cognitive Services to detect Faces
# Prints out JSON

import os
import sys
import json
import requests

# Azure endpoint and access key
endpoint="southeastasia.api.cognitive.microsoft.com"

azure_subscription_key=""

try:
	input_file = sys.argv[1]
except:
	print "Please provide a filename on the commandline"
	exit(1)

request_url = "https://" + endpoint + "/vision/v1.0/analyze"


headers = {'Content-type': 'application/octet-stream', 'Host': endpoint, 'Ocp-Apim-Subscription-Key': azure_subscription_key}
params = {'visualFeatures': 'Faces'}

# data = {"url": image_url}

# response=requests.post(endpoint, params=params, data=json.dumps(data), headers=headers)

# with open(input_file, 'rb') as f: response = requests.post(endpoint, params=params, data=json.dumps(data), headers=headers, files={'image': f})

with open(input_file, mode='rb') as file_handle:
    file_content = file_handle.read()

    response = requests.post(request_url, params=params, headers=headers, data=file_content)

vision=True
detected=True

# Did we get JSON back ?
try:
	json_data = json.loads(response.text)

except:
	vision=False

try:
    detected_faces = json_data["faces"]
except:
    detected=False

# print detected_faces

for face in detected_faces:
    print face
