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


def header(txt):
    print("-" * 40)
    print(txt.center(40))
    print("-" * 40)


def menu(list1):
    header("Main Menu")
    c = 1
    for item in list1:
        print(f"{c} - {item}")
        c+= 1


def record_people():
    print(people)


def signin():
    people.append(str(input("Type your name: ")))
    people.append(int(input("type your age: ")))

people = []