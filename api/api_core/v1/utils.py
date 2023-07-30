import json
import os
from datetime import datetime, timedelta

from jose import jwe

SECRET = os.environ.get("APP_SECURITY_KEY")


def generate_jwt():
    data_ = {
        "valid_true": str(datetime.now() + timedelta(minutes=1)),
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


def decode_jwe(jwt):
    data = jwe.decrypt(
        jwt,
        SECRET
    )
    return json.loads(data)
