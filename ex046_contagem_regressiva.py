#programa que mostra na tela contagem regressiva para estouro de fogos
#de 10 a 0 com pausa de 1 segundo
from time import sleep
print("+---" * 20)
inicio = input("Vamos iniciar a contagem regressiva!")
print("+---" * 20)
for c in range(10,-1,-1):
    print(c, end = " ")
    sleep(1)
print("Feliz ano novo!!!")
