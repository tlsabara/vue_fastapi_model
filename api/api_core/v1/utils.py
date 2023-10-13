import json
import os
from datetime import datetime, timedelta

from jose import jwe

SECRET = os.environ.get("APP_SECURITY_KEY")


def generate_jwt() -> bytes:
    """Function to generate a JWE token for authenticaiton
    """
    data_ = {
        "valid_true": str(datetime.now() + timedelta(hours=1)),
        "resources": {
            "groups": ["get", "post"],
            "users": ["get"]
        }
    }

    return jwe.encrypt(
        json.dumps(data_).encode("utf-8"),
        SECRET,
        algorithm="dir",
        encryption='A256GCM'
    )


def decode_jwe(jwt) -> dict:
    """Function to decrypt a JWE authenticaion token
    """
    data = jwe.decrypt(
        jwt,
        SECRET
    )
    return json.loads(data)
