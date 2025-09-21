#!/usr/bin/env python3
"""
Main application module.
This file demonstrates basic Python code structure for CodeQL analysis.
"""

import os
import sys


def get_config():
    """Get application configuration."""
    # This will trigger the hardcoded API key detection
    api_key = "DUMMY_SECRET_KEY_abc123"
    
    config = {
        "api_key": api_key,
        "debug": False,
        "version": "1.0.0"
    }
    
    return config


def main():
    """Main application entry point."""
    config = get_config()
    
    print(f"Application version: {config['version']}")
    print("Application started successfully")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())