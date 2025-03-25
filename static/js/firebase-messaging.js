// /static/js/firebase-messaging.js
import firebase from 'firebase/app';
import 'firebase/messaging';

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",              // Replace with your API key
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",  // Replace with your project ID
  projectId: "YOUR_PROJECT_ID",        // Replace with your project ID
  storageBucket: "YOUR_PROJECT_ID.appspot.com",  // Replace with your project ID
  messagingSenderId: "YOUR_SENDER_ID",  // Replace with your sender ID
  appId: "YOUR_APP_ID",                // Replace with your app ID
  measurementId: "YOUR_MEASUREMENT_ID" // Replace with your measurement ID
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize Firebase Cloud Messaging
const messaging = firebase.messaging();

// Request permission to send notifications
function requestNotificationPermission() {
  messaging.requestPermission().then(function() {
    return messaging.getToken();
  }).then(function(token) {
    console.log("Firebase token: ", token);
    // You can save the token in your backend here
  }).catch(function(err) {
    console.log("Permission denied or error: ", err);
  });
}

// Handle background push notifications
messaging.setBackgroundMessageHandler(function(payload) {
  const title = payload.notification.title;
  const options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  };
  return self.registration.showNotification(title, options);
});

// Request permission on page load
if ('Notification' in window && navigator.serviceWorker) {
  requestNotificationPermission();
}
