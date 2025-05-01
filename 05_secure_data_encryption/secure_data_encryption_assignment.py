import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# ------------------------------
# Generate a Fernet Key for encryption (could be session-based)
# ------------------------------
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()
fernet = Fernet(st.session_state.fernet_key)

# ------------------------------
# In-memory storage
# ------------------------------
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

# Track failed attempts per session
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# Track if user is authorized
if "authorized" not in st.session_state:
    st.session_state.authorized = True

# ------------------------------
# Utility Functions
# ------------------------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_text(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt_text(ciphertext):
    return fernet.decrypt(ciphertext.encode()).decode()

# ------------------------------
# Pages
# ------------------------------
def home():
    st.title("🔐 Secure Data Encryption System")
    st.write("Select an option below:")
    if st.button("Store New Data"):
        st.session_state.page = "store"
    if st.button("Retrieve Data"):
        st.session_state.page = "retrieve"

def store_data():
    st.title("📥 Store New Data")
    text = st.text_area("Enter the text to encrypt:")
    passkey = st.text_input("Enter a passkey:", type="password")
    data_id = st.text_input("Enter a unique ID for this data:")

    if st.button("Encrypt and Store"):
        if data_id in st.session_state.stored_data:
            st.error("This ID already exists. Please use a unique one.")
            return
        encrypted = encrypt_text(text)
        hashed_key = hash_passkey(passkey)
        st.session_state.stored_data[data_id] = {
            "encrypted_text": encrypted,
            "passkey": hashed_key
        }
        st.success("Data encrypted and stored successfully!")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

def retrieve_data():
    if not st.session_state.authorized:
        st.session_state.page = "login"
        return

    st.title("📤 Retrieve Encrypted Data")
    data_id = st.text_input("Enter the data ID:")
    passkey = st.text_input("Enter the passkey:", type="password")

    if st.button("Decrypt"):
        data = st.session_state.stored_data.get(data_id)
        if not data:
            st.error("No data found with that ID.")
            return

        hashed_input_key = hash_passkey(passkey)
        if hashed_input_key == data["passkey"]:
            decrypted = decrypt_text(data["encrypted_text"])
            st.success("Data decrypted successfully!")
            st.code(decrypted)
            st.session_state.failed_attempts = 0  # Reset on success
        else:
            st.session_state.failed_attempts += 1
            st.error(f"Incorrect passkey! Attempts: {st.session_state.failed_attempts}/3")
            if st.session_state.failed_attempts >= 3:
                st.session_state.authorized = False
                st.session_state.page = "login"

    if st.button("⬅ Back"):
        st.session_state.page = "home"

def login():
    st.title("🔐 Reauthorize to Continue")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":  # Very basic auth
            st.success("Login successful!")
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.session_state.page = "home"
        else:
            st.error("Invalid credentials.")

# ------------------------------
# Page Routing
# ------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home()
elif st.session_state.page == "store":
    store_data()
elif st.session_state.page == "retrieve":
    retrieve_data()
elif st.session_state.page == "login":
    login()
