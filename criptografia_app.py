import re

# Constantes
MIN_USUARIO_LENGTH = 3
MAX_USUARIO_LENGTH = 30
MAX_MENSAGEM_LENGTH = 70


def validar_usuario(usuario):
    """Verifica se o nome de usuário é válido."""
    usuario = usuario.strip()
    if len(usuario) < MIN_USUARIO_LENGTH or len(usuario) > MAX_USUARIO_LENGTH:
        return False
    if not usuario.isalpha() or not usuario[0].isupper():
        return False
    return True


def validar_senha(usuario, senha):
    """Verifica se a senha é válida."""
    senha = senha.strip()
    if len(senha) < 10:
        return False
    if usuario.lower() in senha.lower():
        return False
    if not re.search(r"\d", senha):  # Verifica se há pelo menos um número
        return False
    if not re.search(r"[A-Z]", senha):  # Verifica se há pelo menos uma letra maiúscula
        return False
    if not re.search(r"[a-z]", senha):  # Verifica se há pelo menos uma letra minúscula
        return False
    if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?~`]", senha):  # Verifica se há pelo menos um caractere especial
        return False
    return True


def validar_mensagem(mensagem):
    """Verifica se a mensagem é válida."""
    mensagem = mensagem.strip()
    if len(mensagem) == 0 or len(mensagem) > MAX_MENSAGEM_LENGTH:
        return False
    if not re.match(r"^[ -~]+$", mensagem):  # Verifica se a mensagem contém apenas caracteres ASCII
        return False
    return True
