texto = "Este é um curso que eu estou estudando"
print(texto[3:17])#exibe os espaços de 3 a 16
print(texto[:10])#exibe os espaços do início até 9
print(texto[15:])#exibe os espaços de 15 até o fim
print(texto[8::3])#exibe os espaços de 8 até o fim pulando de 3 em 3
print(len(texto))#conta quantos espaços há no que for digitado
print(texto.count("o"))#conta quantas vezes tem a letra o
print(texto.find("que"))#mostra em que posição inicia a palavra que
print(texto.find("android"))#resultado -1 pois não tem a palavra
print(texto.upper())#mostra tudo maiúsculo
print(texto.lower())#mostra tudo minúsculo
print(texto.capitalize())#mostra o início do texto com maiúsculo
print(texto.title())#mostra todas as palavras iniciando maiúsculo
texto.strip() #remove espaços
texto.rstrip() #remove espaços direita
texto.lstrip() #remove espaços esquerda
print(texto.split())#divide o texto
print("""Agora vamos fazer um teste com um texto bem
longo. Temos que ocupar o máximo possível para que
esta funcionalidade possa surgir efeito. Na verdade
eu estou apenas enchendo linguiça aqui. Então vamos
continuar""")#imprime como está sendo montado
texto = texto.replace("estudando","esperando")#substitui na variável
print(texto)
print("curso" in texto)#verifica se há ou não a palavra
print("android" in texto)
print(texto.split())#divide o texto




