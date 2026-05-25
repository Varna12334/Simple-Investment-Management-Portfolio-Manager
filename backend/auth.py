import os
import hashlib
import pandas as pd
from config import Config

class AuthManager:
    def __init__(self):
        self.csv_path = Config.USERS_DB_PATH
        self.columns = ['Username', 'PasswordHash', 'Salt']
        self._initialize_auth_db()

    def _initialize_auth_db(self):
        """Ensures the data directory and user registry file exist."""
        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
        if not os.path.exists(self.csv_path):
            pd.DataFrame(columns=self.columns).to_csv(self.csv_path, index=False)

    def _hash_password(self, password, salt=None):
        """Hashes a password securely using SHA-256 with an individual salt."""
        if salt is None:
            salt = os.urandom(16).hex()
        
        # Combine salt and password
        salted_pass = password + salt
        hash_obj = hashlib.sha256(salted_pass.encode())
        return hash_obj.hexdigest(), salt

    def register_user(self, username, password):
        """Registers a new user if the username isn't taken."""
        df = pd.read_csv(self.csv_path)
        
        if username in df['Username'].values:
            return False, "Username already exists."
        
        p_hash, salt = self._hash_password(password)
        
        new_user = pd.DataFrame([{
            'Username': username,
            'PasswordHash': p_hash,
            'Salt': salt
        }])
        
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(self.csv_path, index=False)
        return True, "Registration successful."

    def authenticate_user(self, username, password):
        """Verifies provided credentials against the stored hashes."""
        df = pd.read_csv(self.csv_path)
        
        user_rows = df[df['Username'] == username]
        if user_rows.empty:
            return False, "Invalid username or password."
            
        stored_hash = user_rows.iloc[0]['PasswordHash']
        stored_salt = user_rows.iloc[0]['Salt']
        
        # Re-hash the incoming password with the original salt
        check_hash, _ = self._hash_password(password, stored_salt)
        
        if check_hash == stored_hash:
            return True, "Authentication verified."
        return False, "Invalid username or password."
