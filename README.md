# Sample Python Application

A simple Python application to demonstrate CodeQL security analysis.

## Purpose

This repository contains sample Python code with intentional security vulnerabilities (hardcoded API keys) to test CodeQL analysis capabilities.

## Files

- `app.py` - Main application file with API client
- `config.py` - Configuration module with hardcoded secrets
- `utils.py` - Utility functions with security issues

## Security Issues

The code intentionally contains hardcoded API keys following the pattern `DUMMY_SECRET_KEY_[A-Za-z0-9]+` which should be detected by the custom CodeQL query.

## Running the Application

```bash
python app.py
```

Note: This is for demonstration purposes only. The API endpoints are fictional.