import jwt
import datetime
import uuid

from django_auth.config import JWT_SECRET

def get_access_token(payload: dict):
    time = datetime.datetime.now()
    payload["iat"] = time
    payload["exp"] =  time + datetime.timedelta(0, 30)
    access_token = jwt.encode(payload, JWT_SECRET, "HS256")
    return access_token

def decode_access_token(token: str):
    return jwt.decode(token, JWT_SECRET,"HS256" )

def get_refresh_token():
    return uuid.uuid4()