import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def authenticate():
    credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/photoslibrary.readonly'])

    # Check if the credentials are expired, refresh if necessary
    if credentials.expired:
        credentials.refresh(Request())

    return credentials

def list_albums():
    credentials = authenticate()
    service = build('photoslibrary', 'v1', credentials=credentials)

    albums = service.albums().list().execute()
    
    if 'albums' in albums:
        for album in albums['albums']:
            print(f"Album: {album['title']}, ID: {album['id']}")

if __name__ == "__main__":
    list_albums()

