import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from urllib.parse import urlparse, parse_qs
import http.server, webbrowser

from django.http import HttpRequest, HttpResponseRedirect

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
# File that contains the OAuth 2.0 information for this application,
# including its client_id and client_secret.
CLIENT_SECRETS_FILE = "credentials.json"


# def main():
"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""

def authorize(request):
    """
    create the authorization request. That request sets parameters
    that identify your application and define the permissions that the
    user will be asked to grant to your application
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # retrieve the client ID from the credentials.json file
            flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            # indicate where the API server will redirect the user after the
            # user completes the authorization flow
            flow.redirect_uri = 'https://8000-mtelewa-fitnesstracker-7ihzqt4w0n6.ws.codeinstitute-ide.net/'

            # Generate URL for request to Google's OAuth 2.0 server
            authorization_url, state = flow.authorization_url(
                # Enable offline access so that you can refresh an access token without
                # re-prompting the user for permission. Recommended for web server apps.
                access_type='offline',
                # Optional, enable incremental authorization. Recommended as a best practice.
                include_granted_scopes='true',
                # Optional, set prompt to 'consent' will prompt the user for consent
                prompt='consent')
            
            request.session['state'] = state
            print(request.session['state'])

      
    return HttpResponseRedirect(authorization_url)



    # def oauth2callback():
        



            # # authorization_response = request.build_absolute_uri()
            # authorization_response = request.build_absolute_uri()
            # flow.fetch_token(authorization_response=authorization_response)

            # # Store the credentials in the database.
            # credentials = flow.credentials
            # # Save the credentials for the next run
            # with open("token.json", "w") as token:
            #   token.write(credentials.to_json())

    # try:
    #     service = build("calendar", "v3", credentials=credentials)

    #     print('teee')

    #     # Call the Calendar API
    #     now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    #     print("Getting the upcoming 10 events")
    #     events_result = (
    #         service.events()
    #         .list(
    #             calendarId="primary",
    #             timeMin=now,
    #             maxResults=10,
    #             singleEvents=True,
    #             orderBy="startTime",
    #         )
    #         .execute()
    #     )
    #     events = events_result.get("items", [])

    #     if not events:
    #         print("No upcoming events found.")
    #         return

    #     # Prints the start and name of the next 10 events
    #     for event in events:
    #         start = event["start"].get("dateTime", event["start"].get("date"))
    #         print(start, event["summary"])

    # except HttpError as error:
    #     print(f"An error occurred: {error}")


if __name__ == "__main__":
    authorize()