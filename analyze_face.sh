#!/usr/bin/bash
# Takes an image and gives you a JSON object with face: gender, age etc.

# Azure API endpoint for computer vision
endpoint=""

# Your subscription key
azure_subscription_key=""

pic=$1

curl -H "Content-Type: application/octet-stream" -H "Host: $endpoint" -H "Ocp-Apim-Subscription-Key: $azure_subscription_key" --data-binary @$pic "https://$endpoint/vision/v1.0/analyze?visualFeatures=Faces"

