#programa que leia 2 números inteiros e compare-os mostrando mensagem
#primeiro valor é maior, segundo valor é maior, não existe valor maior. são iguais
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
print("+---" * 20)
if num1 > num2:
    print("A primeira opção é maior")
elif num1 < num2:
    print("Asegunda opção é maior")
else:
    print("Não há maior. Os números são iguais")
print("+---" * 20)
