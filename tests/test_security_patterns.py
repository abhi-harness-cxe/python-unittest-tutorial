"""
This is a test file containing dummy patterns for security scanning tests.
These are NOT real credentials and should NEVER be used in production.
"""

# Test patterns for API keys (dummy data)
DUMMY_API_KEY = "sk_test_1234567890abcdefghijklmnop"
DUMMY_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
DUMMY_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Test patterns for authentication (dummy data)
DUMMY_BASIC_AUTH = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="  # base64("username:password")
DUMMY_BEARER_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Test patterns for other common sensitive data (dummy data)
DUMMY_EMAIL = "test.user@example.com"
DUMMY_CREDIT_CARD = "4111-1111-1111-1111"  # Test credit card number
DUMMY_SSN = "123-45-6789"  # Test SSN

# This is not a real secret, just a test pattern
 # Example fix for a potential SQL injection vulnerability using parameterized queries
import sqlite3

def safe_query(db_connection, user_input):
    cursor = db_connection.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (user_input,))
    return cursor.fetchall()

def test_dummy_security_patterns():
    """Dummy test function to verify test patterns are detected."""
    assert True, "This is just a dummy test for security pattern scanning"
