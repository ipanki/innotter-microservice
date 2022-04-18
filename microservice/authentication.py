import jwt
from fastapi import Request, HTTPException
from microservice import config


def auth(request: Request):
    authorization_header = request.headers.get('Authorization')
    if not authorization_header:
        raise HTTPException(status_code=403, detail='Authorization header missing')
    try:
        access_token = authorization_header.split(' ')[1]
        payload = jwt.decode(
            access_token, config.SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        request.state.user_id = user_id

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail='Access_token expired')
    except IndexError:
        raise HTTPException(status_code=403, detail='Token prefix missing')