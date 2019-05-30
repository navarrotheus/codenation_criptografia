import requests

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numero_casas = 5

def decifrar(string)
    mensagem = ''
    for c in string:
        c_index = alfabeto.index(c)
        mensagem += alfabeto[(c_index - numero_casas) % len(alfabeto)]
    return mensagem

decifrar()



        
        


