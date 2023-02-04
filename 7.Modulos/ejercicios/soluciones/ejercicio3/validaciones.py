def validar_email(email:str) -> bool:
    if not email.startswith('@') and email.endswith('@gmail.com'):
        return True
    return False