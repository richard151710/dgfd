# Python Demo Application

This is a simple Python application used to demonstrate CodeQL analysis capabilities.

## Purpose

This repository contains:
- Python source code for CodeQL analysis
- Custom CodeQL queries for security analysis
- GitHub Actions workflow for automated security scanning

## Files

- `main.py` - Main application entry point
- `utils.py` - Utility functions and classes
- `codeql-custom-queries/python/hardcoded-api-key.ql` - Custom CodeQL query for detecting hardcoded API keys

## Security Analysis

The CodeQL analysis will detect security issues such as hardcoded API keys in the source code.

## Running the Application

```bash
python3 main.py
```