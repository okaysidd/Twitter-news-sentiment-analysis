from apiclient.discovery import build

API_KEY = ""
API = "Google Drive API"
VERSION = ""
SERVICE = build(API, VERSION, developerKey=API_KEY)
