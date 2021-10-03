def concat(password: str, secret: str) -> str:
    return password + secret
    
def mix_password(password: str, secret: str) -> str:
    if password and secret:
        return concat(password[0], secret[0]) + mix_password(password[1:], secret[1:])
    elif password and not secret:
        return password
    elif secret and not password:
        return secret
    else:
        return ""