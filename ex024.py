#crie um programa que leia nome de cidade e diga se ela começa ou não
#com o nome "santo"
cidade = str(input("Em que cidade você nasceu: ")).strip()
print(cidade[:5].upper() =="SANTO")
