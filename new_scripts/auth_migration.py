import base64
import time
from typing import Dict
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

# Configuration for both auth methods
API_URL = "https://api.elections.kalshi.com"

# ---------------- DEPRECATED: Username/Password Authentication ----------------
EMAIL = "your.email@example.com"
PASSWORD = "your_password"


def legacy_login(email: str, password: str) -> str:
    """
    DEPRECATED: Legacy authentication using email/password.
    Will be removed in future versions.

    Args:
        email: User's email address
        password: User's password

    Returns:
        str: Authentication token if successful, None otherwise
    """
    response = requests.post(
        f"{API_URL}/trade-api/v2/login",
        json={"email": email, "password": password},
    )
    if response.status_code == 200:
        return response.json()["token"]
    return None


# ---------------- NEW: API Key Authentication ----------------
PRIVATE_KEY_PATH = "path/to/private_key.pem"
KEY_ID = "your_key_id"


class KalshiAuth:
    """
    New authentication class using API keys.
    Handles signing requests with RSA-PSS signatures.
    """

    def __init__(self, private_key_path: str, key_id: str):
        """
        Initialize the auth handler with API key credentials.

        Args:
            private_key_path: Path to the RSA private key file (PEM format)
            key_id: API key identifier provided by Kalshi
        """
        self.key_id = key_id
        self.private_key = self._load_private_key(private_key_path)

    def _load_private_key(self, file_path: str) -> rsa.RSAPrivateKey:
        """
        Load RSA private key from PEM file.

        Args:
            file_path: Path to the private key file

        Returns:
            RSAPrivateKey: Loaded private key object
        """
        with open(file_path, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(), password=None, backend=default_backend()
            )

    def _sign_message(self, message: str) -> str:
        """
        Sign a message using RSA-PSS.

        Args:
            message: Message to sign

        Returns:
            str: Base64-encoded signature
        """
        try:
            signature = self.private_key.sign(
                message.encode("utf-8"),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.DIGEST_LENGTH,
                ),
                hashes.SHA256(),
            )
            return base64.b64encode(signature).decode("utf-8")
        except InvalidSignature as e:
            raise ValueError("Failed to sign message") from e

    def get_auth_headers(self, method: str, path: str) -> Dict[str, str]:
        """
        Generate authentication headers for an API request.

        Args:
            method: HTTP method (GET, POST, etc.)
            path: API endpoint path

        Returns:
            Dict[str, str]: Headers to include with the API request
        """
        timestamp = str(int(time.time() * 1000))
        message = timestamp + method + path

        return {
            "KALSHI-ACCESS-KEY": self.key_id,
            "KALSHI-ACCESS-SIGNATURE": self._sign_message(message),
            "KALSHI-ACCESS-TIMESTAMP": timestamp,
            "Content-Type": "application/json",
        }


# ---------------- Example Usage ----------------
def example_api_request():
    """Example showing both authentication methods side by side."""

    # DEPRECATED: Old way using username/password
    token = legacy_login(EMAIL, PASSWORD)
    deprecated_headers = {"Authorization": f"Bearer {token}"}

    # NEW: Using API key authentication
    auth = KalshiAuth(PRIVATE_KEY_PATH, KEY_ID)

    # Example API request using the new authentication
    path = "/trade-api/v2/events/KXBTCD-24DEC0417"
    new_headers = auth.get_auth_headers("GET", path)
    try:
        response = requests.get(
            f"{API_URL}{path}",
            headers=new_headers,
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    if response.status_code != 200:
        print(f"Error fetching markets: {response.text}")
        return None

    return response.json()


if __name__ == "__main__":
    # Example of how to use the new authentication
    try:
        auth = KalshiAuth(PRIVATE_KEY_PATH, KEY_ID)
        headers = auth.get_auth_headers("GET", "/trade-api/v2/markets")
        print("Successfully generated auth headers:", headers)
    except Exception as e:
        print(f"Error setting up authentication: {e}")
