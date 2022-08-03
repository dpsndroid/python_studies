#atributos de texto (padrão ANSI)

#estilos do python: 0 = none, 1 = bold, 4 = underline, 7 = negative (inverte)

#cor do texto: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul,
# 35 magenta, 36 ciano, 37 cinza

#cor do fundo: 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul,
# 45 magenta, 46 ciano, 47 cinza

#ORDEM: estilo, texto, fundo
#NÃO FUNCIONOU NO IDLE, USEI O PYCHARM

print("\033[30;43m Olá Mundo \033[m")
print("\033[7;30;43m Olá Mundo \033[m")
print("\033[31;40m Olá Mundo \033[m")
print("\033[4;30;43m Olá Mundo \033[m")
print("\033[1;30;47m Olá Mundo \033[m")
print("\033[0;30;43m Olá Mundo \033[m")
print("O final deste texto está \033[1;33mOK\033[m")
cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "amarelo":"\033[33m",
         "pretoebranco":"\033[7;30m"}
nome = "Daniel"
print("Olá {}{}{}".format(cores["pretoebranco"], nome, cores["limpa"]))