import pytest
from criptografia_app import validar_usuario, validar_senha, validar_mensagem

# Testes para a função validar_usuario

def test_validar_usuario_com_menos_de_tres_letras():
    assert validar_usuario("Lu") == False

def test_validar_usuario_com_mais_de_trinta_letras():
    assert validar_usuario("FelipeRibeiroDeOliveiraLimaSilvaMeloSouza") == False

def test_validar_usuario_que_nao_comeca_com_letra_maiuscula():
    assert validar_usuario("usuario") == False

def test_validar_usuario_valido():
    assert validar_usuario("Felipe") == True


# Testes para a função validar_senha

def test_validar_senha_com_menos_de_dez_caracteres():
    assert validar_senha("felipe", "Senha123") == False

def test_validar_senha_sem_letra_maiuscula():
    assert validar_senha("felipe", "senha123!@") == False

def test_validar_senha_sem_letra_minuscula():
    assert validar_senha("felipe", "SENHA123!@") == False

def test_validar_senha_sem_numero():
    assert validar_senha("felipe", "SenhaTeste!") == False

def test_validar_senha_com_nome_de_usuario():
    assert validar_senha("felipe", "Felipe123!") == False

def test_validar_senha_valida():
    assert validar_senha("felipe", "Senha123!@") == True


# Testes para a função validar_mensagem

def test_validar_mensagem_com_mais_de_setenta_caracteres():
    assert validar_mensagem("Esta mensagem tem mais de setenta caracteres e não deve ser válida.") == False

def test_validar_mensagem_vazia():
    assert validar_mensagem("") == False

def test_validar_mensagem_com_caractere_nao_ascii():
    assert validar_mensagem("Mensagem com caractere não-ascii: áéíóú") == False

def test_validar_mensagem_com_arroba():
    assert validar_mensagem("Esta mensagem contém um @ e deve ser inválida.") == False

def test_validar_mensagem_valida():
    assert validar_mensagem("Esta é uma mensagem válida.") == False



