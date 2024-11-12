import json
import os
import logging
import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(input, context):
    logger.info(f"FunctionHandler received: {input}")

    # Deserialize the input as JSON
    # payload = json.dumps({'text': "Issue Created: test"})
    payload = json.dumps({'text': f"Issue Created: {input['issue']['html_url']}"})

    # Send the request to Slack
    client = requests.Session()
    web_request = requests.Request(
        method="POST",
        url=os.getenv("SLACK_URL"),
        data=payload,
        headers={'Content-Type': 'application/json'}
    ).prepare()

    response = client.send(web_request)
    
    # Return response content
    return response.text
