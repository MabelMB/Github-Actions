import random

def validar_password(password):
    if len(password) < 8:
       return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if password.lower() in {"password", "123456", "qwerty", "abc123"}:
        return False

    return True