import jwt
import json
import requests

def isValidToken(request, sub):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        print("Error: Authorization header is missing")
        return False

    token = auth_header.replace("Bearer ", "", 1)

    try:
        validation = jwt.decode(token, "12345", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("Error: JWT Token has expired")
        return False
    except jwt.InvalidTokenError:
        print("Error: Invalid JWT Token")
        return False

    if validation.get("iss") != "ingesis.uniquindio.edu.co":
        print("Error: The token issuer is not valid")
        return False

    if sub != "":
        sub_from_token = validation.get("sub")
        if sub_from_token is None:
            print("Error: User claim 'sub' is missing in the token")
            return False
        if sub_from_token != sub:
            print("Error: User in token does not match expected user")
            return False

    return True
