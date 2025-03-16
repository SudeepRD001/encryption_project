from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import EncryptedMessage
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

# File paths for RSA keys
PRIVATE_KEY_PATH = "private.pem"
PUBLIC_KEY_PATH = "public.pem"

# ✅ Function to generate and load RSA keys
def load_or_generate_keys():
    """Generate RSA keys if they don't exist and load them."""
    if not (os.path.exists(PRIVATE_KEY_PATH) and os.path.exists(PUBLIC_KEY_PATH)):
        print("🔑 Generating new RSA keys...")  # Debugging log
        key = RSA.generate(2048)
        with open(PRIVATE_KEY_PATH, "wb") as private_file:
            private_file.write(key.export_key())
        with open(PUBLIC_KEY_PATH, "wb") as public_file:
            public_file.write(key.publickey().export_key())

    try:
        # Load keys from file
        with open(PRIVATE_KEY_PATH, "rb") as private_file:
            private_key = RSA.import_key(private_file.read())
        with open(PUBLIC_KEY_PATH, "rb") as public_file:
            public_key = RSA.import_key(public_file.read())

        print("✅ RSA Keys Loaded Successfully")  # Debugging log
        return private_key, public_key

    except Exception as e:
        print(f"❌ Error loading keys: {str(e)}")  # Debugging log
        return None, None  # Ensure function always returns something

# ✅ Load keys globally
PRIVATE_KEY, PUBLIC_KEY = load_or_generate_keys()

# ✅ Ensure keys are valid before proceeding
if not PRIVATE_KEY or not PUBLIC_KEY:
    raise RuntimeError("RSA Key Loading Failed! Check the logs.")

# ✅ Home Page Redirect
def home_view(request):
    return redirect(reverse('encrypt'))  # ✅ Uses reverse() for better URL management

# ✅ Encryption View (Restricted to logged-in users)
@login_required
def encrypt_view(request):
    if request.method == "POST":
        message = request.POST.get("plaintext", "").strip()  # ✅ Matches frontend field name
        if not message:
            return JsonResponse({"error": "No message provided"}, status=400)

        if not PUBLIC_KEY:
            return JsonResponse({"error": "Encryption failed: RSA public key is missing"}, status=500)

        try:
            # Encrypt message using RSA PKCS1_OAEP
            cipher = PKCS1_OAEP.new(PUBLIC_KEY)
            encrypted_bytes = cipher.encrypt(message.encode())

            # Encode in base64 to send over HTTP
            encrypted_text = base64.b64encode(encrypted_bytes).decode()

            # ✅ Save encrypted message to DB (Optional)
            encrypted_message = EncryptedMessage.objects.create(encrypted_text=encrypted_text)

            return JsonResponse({"encrypted": encrypted_text})
        except Exception as e:
            return JsonResponse({"error": f"Encryption failed: {str(e)}"}, status=500)

    return render(request, "encrypt.html")

# ✅ Decryption View (Restricted to logged-in users)
@login_required
def decrypt_view(request):
    if request.method == "POST":
        encrypted_text = request.POST.get("encrypted_text", "").strip()
        if not encrypted_text:
            return JsonResponse({"error": "No encrypted text provided"}, status=400)

        try:
            # ✅ Ensure keys are loaded
            global PRIVATE_KEY, PUBLIC_KEY
            if not PRIVATE_KEY or not PUBLIC_KEY:
                PRIVATE_KEY, PUBLIC_KEY = load_or_generate_keys()

            # Decode base64 and decrypt
            encrypted_bytes = base64.b64decode(encrypted_text)
            cipher = PKCS1_OAEP.new(PRIVATE_KEY)
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
            decrypted_text = decrypted_bytes.decode()

            return JsonResponse({"decrypted": decrypted_text})
        except (ValueError, TypeError):
            return JsonResponse({"error": "Invalid encryption format or incorrect key."}, status=400)
        except Exception as e:
            print(f"Decryption error: {str(e)}")  # ✅ Debugging Log
            return JsonResponse({"error": f"Decryption failed: {str(e)}"}, status=500)

    return render(request, "decrypt.html")

# ✅ Result View to Display Encrypted/Decrypted Text
@login_required
def result_view(request, message_id=None):
    """Displays the result page with encrypted or decrypted text."""
    message = None

    if message_id:
        message = get_object_or_404(EncryptedMessage, id=message_id)  # ✅ Better Query Handling

    return render(request, "result.html", {"message": message})
