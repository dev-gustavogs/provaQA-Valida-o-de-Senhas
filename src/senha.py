def validar_senha(senha: str, usuario: str) -> bool:
    if len(senha) < 8:
        return False
    if senha.lower() == usuario.lower():
        return False
    if " " in senha:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    return True
