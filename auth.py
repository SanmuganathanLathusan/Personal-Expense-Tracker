import json
import hashlib
from utils import load_data, save_data

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    print("\n--- Register User ---")
    
    username = input("Username: ")
    password = input("Password: ")

    users = load_data(USERS_FILE)

    # Check if username exists
    for user in users:
        if user["username"] == username:
            print("❌ Username already exists.")
            return None

    hashed_pw = hash_password(password)

    new_user = {
        "username": username,
        "password": hashed_pw
    }

    users.append(new_user)
    save_data(USERS_FILE, users)

    print("✅ User registered successfully!")
    return username

def login_user():
    print("\n--- Login ---")
    
    username = input("Username: ")
    password = input("Password: ")

    users = load_data(USERS_FILE)

    hashed_pw = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_pw:
            print("✅ Login successful!")
            return username

    print("❌ Invalid username or password.")
    return None
