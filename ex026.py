#programa que leia uma frase e mostre quantas vezes aparece
#a letra A, em que posição aparece na primeira vez e na última vez
frase = str(input("Digite uma frase qualquer: ")).lower().strip()#recebe o texto em minúsculo e retira os espaços
print("A letra 'A' aparece {} vezes.".format(frase.count("a")))#imprime quantas vezes tem a letra A
print("A primeira letra A aparece na posição {}".format(frase.find("a")+1))#imprime a primeira posição qua aparece a, somado de 1 para a nossa contagem
print("A última letra A aparece na posição {}.".format(frase.rfind("a")+1))#a mesma coisa de cima, mas começa procurando pela direita
