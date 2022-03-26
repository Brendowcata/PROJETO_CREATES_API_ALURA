import re

def cpf_IsValid(cpf):
    return len(cpf) == 11

def nome_IsValid(nome):
    return nome.isalpha()

def rg_IsValid(rg):
    return len(rg) == 9

def celular_IsValid(celular):
    """Verifica se o celular é valido (##) 9####-####"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
            