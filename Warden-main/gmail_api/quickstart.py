from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json
from flask import Flask, render_template, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
name = "google_api"
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

@application.route('/', methods =['GET'])
def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    # This portion remembers user credentials
    #if os.path.exists('token.json'):
        #creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Requires log-in every time.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './gmail_api/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./gmail_api/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    label_results = service.users().labels().list(userId = 'me').execute()
    labels = label_results.get('labels', [])

    message_results = service.users().messages().list(userId = "me", labelIds = ["INBOX"]).execute()
    messages = message_results.get("messages", [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels acquired.')

    if not messages:
        print('No messages found.')
    else:
        i = 0
        output = {}
        output["messages"] = []

        for message in messages:

            message = service.users().messages().get(userId = "me", id = message['id']).execute()
            message = message["snippet"]
            #print some out just to check

            #if conditional check for warnme
            keyphrase = "Please note this message may contain information that some may find upsetting. On "
            if keyphrase in message: 
                message = message.replace(keyphrase, "")
                message = message.split(" ")
                print(message)
                
                date = message[0]
                date_filled = True
                crime = ""
                crime_filled = False
                location = ""
                location_filled = False
                while message:
                    if message[0] == "a":
                        message = message[1:]
                        crime = message[0]
                        crime_filled = True
                        print("CRIME: " + crime)
                    elif message[0] == "at":
                        message = message[1:]
                        location = ""
                        for word in message:
                            if "." in word:
                                location += word
                                location += " "
                                break
                            else:
                                location += word
                                location += " "
                                message = message[1:]
                        location.replace(".","")
                        location.replace("&#39:","")
                        location_filled = True

                    if crime and location and date:
                        output["messages"].append({
                            'title': crime,
                            'location': location,
                            "time" : date,
                        })

                    if date_filled and crime_filled and location_filled:
                        break
                    
                    message = message[1:]

                    
                    
    return output
        

    #deserialize message JSON objects
    #messages = json.loads(str(messages))

if __name__ == '__main__':
    application.run(host="10.142.45.208", port=5000, debug = True)
    #main()

