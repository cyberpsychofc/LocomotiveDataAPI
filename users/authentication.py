import jwt
from rest_framework.exceptions import AuthenticationFailed

def verify_user_token(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['id']
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    except jwt.InvalidSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    except jwt.DecodeError:
        raise AuthenticationFailed("Invalid Token")