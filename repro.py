from google.auth import default
from google.auth._helpers import utcnow
from google.auth.transport.requests import Request
from google.oauth2 import credentials
import datetime

FILENAME = "cred.json"


def export_cred():
    c, _ = default()
    c.refresh(Request())

    with open(FILENAME, "w") as f:
        f.write(c.to_json())
    print(f"Serialized credential that expires in {c.expiry - utcnow()} UTC")


def print_existing_cred():
    c = credentials.Credentials.from_authorized_user_file(FILENAME)
    print(f"{c.valid=}")
    print(f"{c.expired=}")
    print(f"De-serialized credential expires in {c.expiry - utcnow()} UTC")
    print(
        f"De-serialized credential expires in {c.expiry - datetime.datetime.now()} using naive datetime object"
    )


def export_expired_cred():
    c, _ = default()
    c.refresh(Request())

    c.expiry = datetime.datetime.utcnow() - datetime.timedelta(hours=1)

    with open(FILENAME, "w") as f:
        f.write(c.to_json())
    print(f"Serialized credential that expires in {c.expiry - utcnow()} UTC")
