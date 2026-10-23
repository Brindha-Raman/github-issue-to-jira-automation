# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask, request


app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = os.getenv("URL")
    EMAIL_ID = os.getenv("EMAIL_ID")
    API_TOKEN = os.getenv("API_TOKEN")
        
    auth = HTTPBasicAuth(EMAIL_ID, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = request.json
    comment = data["comment"]["body"]
    issue_title = data["issue"]["title"]
    issue_description = data["issue"]["body"]

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": issue_description,
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "TT"
        },
        "issuetype": {
            "id": "10012"
        },
        "summary": issue_title,
    },
    "update": {}
    } )

    #output = response.json()
    
    if comment.strip().lower() == "/jira":
        response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Jira issue will be created if comment includes /jira"

    #return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)