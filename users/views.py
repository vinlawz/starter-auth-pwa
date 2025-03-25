# users/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from app.models import FCMToken
from django.contrib.auth import authenticate, login
from app.utils import send_push_notification  # Import the notification function

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    firebase_token = request.data.get('firebase_token')  # Get Firebase token from frontend

    if not username or not password or not firebase_token:
        return Response({'error': 'All fields are required'}, status=400)

    user = User.objects.create_user(username=username, password=password)

    # Save Firebase Token
    FCMToken.objects.create(user=user, firebase_token=firebase_token)

    # Send Welcome Notification  
    send_push_notification(user, "Welcome!", "Thank you for registering!")

    return Response({'message': 'User registered successfully.'}, status=201)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    firebase_token = request.data.get('firebase_token')  # Get Firebase token from frontend

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'}, status=400)

    login(request, user)

    # Update Firebase Token
    fcm_token, created = FCMToken.objects.get_or_create(user=user)
    fcm_token.firebase_token = firebase_token
    fcm_token.save()

    # Send Login Notification  
    send_push_notification(user, "Login Successful", "You have successfully logged in.")

    return Response({'message': 'User logged in successfully.'})
