#create a mini system using interactive help
#the user types the comand and the manual will appear

c = ("\033[n",        #0 - sem cores
     "\033[0;30;41m",  #1 - vermelho
     "\033[0;30;42m",  #2 - verde
     "\033[0;30;43m",  #3 - amarelo
     "\033[0;30;44m",  #4 - azul
     "\033[0;30;45m",  #5 - roxo
     "\033[7;30m"     #6 - branco
    )

def ajuda(com):
    help(com)


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = "")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end = "")

comando = ""
while True:
    titulo("Sistema de ajuda Pyhelp", 2)
    comando = str(input("Function or Library >"))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("Até logo", 1)