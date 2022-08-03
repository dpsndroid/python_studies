#programa com uma função chamada escreva, receba texto qualquer e mostre
#mensagem com tamanho adaptavel



def deco(message):
    size = len(message) + 4
    print("="*size)
    print(f"  {message}")
    print("="*size)

name = str(input("Type a name: "))

deco(name)

