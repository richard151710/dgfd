#!/usr/bin/env python3
"""
Sample Python application for CodeQL analysis.
This file contains hardcoded API keys that should be detected by CodeQL.
"""

import os
import requests


class APIClient:
    """A simple API client with hardcoded credentials (security issue)."""
    
    def __init__(self):
        # This is a security vulnerability - hardcoded API key
        self.api_key = "DUMMY_SECRET_KEY_abc123"
        self.base_url = "https://api.example.com"
        
    def get_data(self, endpoint):
        """Fetch data from the API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return None


def main():
    """Main function to demonstrate API usage."""
    client = APIClient()
    data = client.get_data("users")
    
    if data:
        print("Successfully retrieved data from API")
    else:
        print("Failed to retrieve data")


if __name__ == "__main__":
    main()