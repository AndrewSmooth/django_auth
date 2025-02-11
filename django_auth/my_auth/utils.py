import jwt
import datetime
import uuid

from django_auth.config import JWT_SECRET

def get_access_token(payload: dict, secret: str=JWT_SECRET, algorithm: str = "HS256"):
    time = datetime.datetime.now()
    payload["iat"] = time
    payload["exp"] =  time + datetime.timedelta(0, 30)
    access_token = jwt.encode(payload, secret, algorithm)
    return access_token

def get_refresh_token():
    return uuid.uuid4()