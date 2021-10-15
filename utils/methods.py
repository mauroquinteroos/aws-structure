import uuid


def generate_token():
    token = uuid.uuid4()
    return str(token)
