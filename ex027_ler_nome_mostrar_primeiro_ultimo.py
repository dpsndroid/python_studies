#programa que leia o nome completo, mostrando o primeiro e o
#ultimo nome separadamente


n = str(input("Digite seu nome completo: ")).strip()#insere texto e retira espaços
nome = n.split()#divide o texto em posições de lista

print("Seu primeiro nome é {}".format(nome[0]))#exibe o primeiro nome na lista
print("Seu último nome é {}".format(nome[len(nome)-1]))#exibe o último nome do comprimento da lista
