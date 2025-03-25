import firebase_admin
from firebase_admin import credentials, auth
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIREBASE_KEY_PATH = os.path.join(BASE_DIR, "miltrack-63988-firebase-adminsdk-fbsvc-d7c7c50ce8.json")


cred = credentials.Certificate(FIREBASE_KEY_PATH)
firebase_admin.initialize_app(cred)
