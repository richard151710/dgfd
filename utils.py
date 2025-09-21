"""
Utility functions for the application.
"""

import os


class ApiClient:
    """Simple API client class."""
    
    def __init__(self, api_key=None):
        """Initialize the API client."""
        self.api_key = api_key or "DUMMY_SECRET_KEY_xyz789"
        self.base_url = "https://api.example.com"
    
    def authenticate(self):
        """Authenticate with the API."""
        if not self.api_key:
            raise ValueError("API key is required")
        
        # Simulate authentication
        return {"authenticated": True, "user": "demo"}
    
    def make_request(self, endpoint):
        """Make a request to the API."""
        if not self.authenticate():
            return None
        
        # Simulate API request
        return {"status": "success", "endpoint": endpoint}


def safe_api_client():
    """Create an API client with environment-based configuration."""
    # This is the secure way - getting from environment
    api_key = os.environ.get("API_KEY")
    return ApiClient(api_key)


def unsafe_api_client():
    """Create an API client with hardcoded credentials - BAD PRACTICE."""
    # This will trigger the CodeQL security alert
    secret_key = "DUMMY_SECRET_KEY_hardcoded123"
    return ApiClient(secret_key)