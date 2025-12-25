"""
Test script to verify the application structure works correctly.
"""
import os
import sys
from unittest.mock import patch

# Add the backend directory to the path so imports work correctly
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)

# Mock environment variables to avoid the need for actual API keys
with patch.dict(os.environ, {
    'OPENAI_API_KEY': 'test-key',
    'QDRANT_URL': 'https://test.qdrant.io:6333',
    'QDRANT_API_KEY': 'test-key',
    'DATABASE_URL': 'postgresql://user:pass@localhost/test',
    'ENVIRONMENT': 'test',
    'CORS_ALLOWED_ORIGINS': 'http://localhost:3000,http://localhost:4000'
}):
    try:
        # Change to the backend directory to make imports work
        os.chdir(backend_path)

        # Try to import the main app
        from src.main import app
        print("SUCCESS: Backend imports successfully")

        # Try to import the services
        from src.services.openai_service import openai_service
        from src.services.qdrant_service import qdrant_service
        print("SUCCESS: Services import successfully")

        # Try to import models
        from src.models.schemas import ChatRequest
        from src.models.database import Base
        print("SUCCESS: Models import successfully")

        # Try to import config
        from src.config import settings
        print(f"SUCCESS: Config loaded: environment = {settings.environment}")

        print("\nSUCCESS: All imports successful! Application structure is correct.")

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)