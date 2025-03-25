# firebase_service.py
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin SDK with your Firebase credentials
cred = credentials.Certificate("C:\\Users\\vinla\\Downloads\\miltrack-63988-firebase-adminsdk-fbsvc-d7c7c50ce8.json")

firebase_admin.initialize_app(cred)

def send_push_notification(fcm_token, title, body):
    """Send a push notification to a user."""
    # Create the message to send
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=fcm_token,  # The FCM token of the user
    )

    try:
        # Send the message via Firebase
        response = messaging.send(message)
        print('Successfully sent message:', response)
    except Exception as e:
        print(f'Error sending message: {e}')
