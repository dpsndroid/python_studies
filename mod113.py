def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Digite um número inteiro válido")
            continue
        except KeyboardInterrupt:
            print("Cancelado pelo usuário")
            return 0
        else:
            return n
        

def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("Digite um número inteiro válido")
            continue
        except KeyboardInterrupt:
            print("Cancelado pelo usuário")
            return 0
        else:
            return n