"""
Utility functions for the application.
"""

import hashlib
import json
from typing import Dict, Any


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_config() -> Dict[str, Any]:
    """Load configuration from a file or return defaults."""
    default_config = {
        "app_name": "Sample App",
        "version": "1.0.0",
        "secret": "DUMMY_SECRET_KEY_pqr678",  # Another hardcoded secret
        "environment": "development"
    }
    
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            return {**default_config, **config}
    except FileNotFoundError:
        return default_config


def validate_api_key(key: str) -> bool:
    """Validate an API key."""
    # Hardcoded validation key - security issue
    valid_key = "DUMMY_SECRET_KEY_stu901"
    return key == valid_key


class SecurityManager:
    """Manages security-related operations."""
    
    def __init__(self):
        # Hardcoded encryption key
        self.encryption_key = "DUMMY_SECRET_KEY_vwx234"
        
    def encrypt_data(self, data: str) -> str:
        """Encrypt data (simplified example)."""
        # This is a very basic example - not real encryption
        return f"encrypted_{data}_{self.encryption_key}"
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt data (simplified example)."""
        # This is a very basic example - not real decryption
        return encrypted_data.replace(f"encrypted_", "").replace(f"_{self.encryption_key}", "")


# Module-level secret
MODULE_SECRET = "DUMMY_SECRET_KEY_yza567"