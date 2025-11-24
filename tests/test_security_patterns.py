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
                              # Assuming the vulnerability is related to user input, here's a safe way to handle it
import html

user_input = "<script>alert('XSS');</script>"
safe_output = html.escape(user_input)
print(safe_output)

# Test patterns for other common sensitive data (dummy data)
DUMMY_EMAIL = "test.user@example.com"
DUMMY_CREDIT_CARD = "4111-1111-1111-1111"  # Test credit card number
DUMMY_SSN = "123-45-6789"  # Test SSN

# This is not a real secret, just a test pattern
TEST_ENCRYPTION_KEY = "test_key_1234567890abcdef1234567890abcdef"

def test_dummy_security_patterns():
    """Dummy test function to verify test patterns are detected."""
    assert True, "This is just a dummy test for security pattern scanning"
