nome = str(input("Qual é o seu nome: "))
if nome == "Daniel":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print("Bom dia, {}!".format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(m))
if m >= 7.0:
    print("Parabéns, você foi aprovado")
else:
    print("Só lamento, tem que estudar mais")
print("Pode seguir para o próximo nível" if m >= 7.0 else "Você é prego")

