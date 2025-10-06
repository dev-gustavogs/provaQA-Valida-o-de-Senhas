import pytest
from src.senha import validar_senha

def test_senha_valida():
    assert validar_senha("Senha123", "usuario") is True

def test_senha_curta():
    assert validar_senha("Sen1", "usuario") is False

def test_senha_sem_maiuscula():
    assert validar_senha("senha123", "usuario") is False

def test_senha_sem_numero():
    assert validar_senha("SenhaTeste", "usuario") is False

def test_senha_com_espaco():
    assert validar_senha("Senha 123", "usuario") is False

def test_senha_igual_usuario():
    assert validar_senha("Usuario", "usuario") is False
