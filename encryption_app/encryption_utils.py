from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64
import os

# ✅ File Paths for RSA Keys
PRIVATE_KEY_FILE = "private_key.pem"
PUBLIC_KEY_FILE = "public_key.pem"

# ✅ RSA Key Handling
def generate_and_store_keys():
    """Generates and stores RSA key pair if not already present."""
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        key_pair = RSA.generate(2048)
        with open(PRIVATE_KEY_FILE, "wb") as priv_file, open(PUBLIC_KEY_FILE, "wb") as pub_file:
            priv_file.write(key_pair.export_key())
            pub_file.write(key_pair.publickey().export_key())

# ✅ Load RSA Keys
def load_keys():
    """Loads RSA keys from files."""
    with open(PRIVATE_KEY_FILE, "rb") as priv_file, open(PUBLIC_KEY_FILE, "rb") as pub_file:
        private_key = RSA.import_key(priv_file.read())
        public_key = RSA.import_key(pub_file.read())
    return private_key, public_key

# ✅ Ensure Keys Exist
generate_and_store_keys()
private_key, public_key = load_keys()

def encrypt_message(message):
    """Encrypts a message using AES + RSA hybrid encryption."""
    aes_key = get_random_bytes(16)  # AES Key
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    # ✅ Encrypt AES key with RSA using OAEP
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # ✅ Return Base64 Encoded Encrypted Data
    return base64.b64encode(encrypted_aes_key + cipher_aes.nonce + tag + ciphertext).decode()

def decrypt_message(encrypted_data):
    """Decrypts an AES-encrypted message using RSA to unlock the AES key."""
    decoded_data = base64.b64decode(encrypted_data)

    # ✅ Extract Components
    encrypted_aes_key, nonce, tag, ciphertext = (
        decoded_data[:256], decoded_data[256:272], decoded_data[272:288], decoded_data[288:]
    )

    # ✅ Decrypt AES Key with RSA OAEP
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # ✅ Decrypt the Message
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return decrypted_message.decode()
