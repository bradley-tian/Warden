from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
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
        for message in messages:
            message = service.users().messages().get(userId = "me", id = message['id']).execute()
            message = message["snippet"]
            #print some out just to check
            print(message)
            print("\n")
            if i > 10:
                break
            i += 1
        

    #deserialize message JSON objects
    #messages = json.loads(str(messages))

if __name__ == '__main__':
    main()

