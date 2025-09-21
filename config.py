"""
Configuration module with various security issues for CodeQL to detect.
"""

# Another hardcoded API key example
SECRET_KEY = "DUMMY_SECRET_KEY_xyz789"

# Database configuration with hardcoded credentials
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "username": "admin",
    "password": "password123",  # Not the pattern we're looking for, but still bad
    "database": "myapp"
}

# API configuration
API_SETTINGS = {
    "api_key": "DUMMY_SECRET_KEY_def456",  # This should be detected
    "timeout": 30,
    "retries": 3
}

class Config:
    """Application configuration class."""
    
    def __init__(self):
        # Yet another hardcoded secret
        self.jwt_secret = "DUMMY_SECRET_KEY_ghi789"
        self.debug = True
        
    def get_api_key(self):
        """Return the API key."""
        return self.jwt_secret


# Function with hardcoded secret
def authenticate_user():
    """Authenticate user with hardcoded key."""
    auth_token = "DUMMY_SECRET_KEY_jkl012"
    return auth_token


# Global variable with secret
MASTER_KEY = "DUMMY_SECRET_KEY_mno345"