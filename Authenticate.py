from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os

############################################################################################################################################
#Authentication function

def authenticate():                                                     #Returns googleapi authentication (new or updated) with Creds, Sheets and Drive
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = None
    if os.path.exists('drive:\\path\\to\\token.json'):
        creds = Credentials.from_authorized_user_file('drive:\\path\\to\\token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "drive:\\path\\to\\secrets_file\\here", SCOPES)
            creds = flow.run_local_server(port=0)
        with open('drive:\\path\\to\\token.json', 'w') as token:
            token.write(creds.to_json())

    return creds, build('sheets', 'v4', credentials=creds), build('drive', 'v3', credentials=creds)

############################################################################################################################################

