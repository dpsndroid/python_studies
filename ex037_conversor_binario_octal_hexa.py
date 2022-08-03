#programa que leia um número inteiro e pedir para escolher qual
#será a base de conversão 1 binário, 2 octal, 3 hexadecimal
num = int(input("Digite um número inteiro qualquer: "))
print("+---" * 20)
print("""Bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")
print("+---" * 20)
opcao = int(input("Escolha uma opção acima: "))
if opcao == 1:
    print("O número {} convertido para binário é {}".format(num,bin(num)[2:]))
elif opcao == 2:
    print("O número {} convertido para octal é {}".format(num,oct(num)[2:]))
elif opcao == 3:
    print("O número {} convertido para hexadecimal é {}".format(num,hex(num)[2:]))
else:
    print("Opção inválida. O programa terminou")
print("+---" * 20)
