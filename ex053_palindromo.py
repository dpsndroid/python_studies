#programa que leia uma frase e diga se ela é um palindromo
#frase que pode ler de trás pra frente e vice versa
print("+---" * 20)
text = str(input("Digite uma frase ou palavra: ")).strip().upper()
palavras = text.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print("+---" * 20)
print("A frase é: ", junto)
print("Seu inverso é: ", inverso)
if junto == inverso:
   print("Temos um palíndromo!")
else:
   print("Não é um palíndromo")
print("+---" * 20)
print("""

OUTRA FORMA

""")
print("+---" * 20)
text = str(input("Digite uma frase ou palavra: ")).strip().upper()
palavras = text.split()
junto = "".join(palavras)
inverso = junto[::-1] #fatiamento de string
print("+---" * 20)
print("O inverso de {} é {}".format(junto, inverso))
if junto == inverso:
   print("Temos um palíndromo!")
else:
   print("Não é um palíndromo")
print("+---" * 20)
