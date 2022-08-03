#refaça o desafio 9, com uma tabuada de um número escolhido, mas com laço for
print("{:=^20}".format("TABUADA"))
print("+---" * 20)
num = int(input("Digite um número inteiro: "))
print("+---" * 20)
for c in range(1,11):
    print("{} x {:2} = {:2}".format(num, c, num * c))
print("+---" * 20)
print("Aprendeu?")
