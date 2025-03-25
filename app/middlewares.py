import firebase_admin
from firebase_admin import auth, credentials
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

User = get_user_model()

# ✅ Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\vinla\Downloads\miltrack-63988-firebase-adminsdk-fbsvc-d7c7c50ce8.json")  
    firebase_admin.initialize_app(cred)

class FirebaseAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """Extracts Firebase token, verifies it, and attaches user to request."""
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return None  # No token provided, continue request

        token = auth_header.split(" ")[-1]  # Extract token

        try:
            decoded_token = auth.verify_id_token(token)
            firebase_uid = decoded_token.get("uid")
            email = decoded_token.get("email")

            if not firebase_uid or not email:
                return JsonResponse({"error": "Invalid Firebase token"}, status=401)

            # ✅ Ensure user exists or create a new one
            user, created = User.objects.get_or_create(
                username=firebase_uid,
                defaults={"email": email},
            )

            request.user = user  # Attach user to request

        except auth.InvalidIdTokenError:
            return JsonResponse({"error": "Invalid Firebase ID token"}, status=401)
        except auth.ExpiredIdTokenError:
            return JsonResponse({"error": "Expired Firebase ID token"}, status=401)
        except auth.RevokedIdTokenError:
            return JsonResponse({"error": "Revoked Firebase ID token"}, status=401)
        except Exception as e:
            return JsonResponse({"error": f"Authentication failed: {str(e)}"}, status=401)
