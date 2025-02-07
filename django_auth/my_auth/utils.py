import jwt


def get_access_token(payload: dict, secret: str, algorithm: str = "HS256"):
    access_token = jwt.encode({"some": "payload"}, "secret", algorithm)
    return access_token

# print(encoded)
# decoded = jwt.decode(encoded, "secret", algorithms=["HS256"])
# print(decoded)