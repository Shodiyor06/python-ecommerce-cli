from hashlib import sha256


def make_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()
