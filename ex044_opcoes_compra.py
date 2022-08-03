#programa que calcula valor a ser pago pelo produto considerando
#o preço normal e a condição de pagamento. à vista dinheiro ou cheque
#10% de desconto. à vista cartão 5% desconto. 2x cartao preço normal
#3x ou mais cartao 20% de juros
prod = float(input("Quanto custa sua compra: R$ "))
print("+---" * 20)
print("""    CONDIÇÕES DE PAGAMENTO:
[1] À vista em dinheiro ou cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Parcelado em 2 vezes (preço normal)
[4] Parcelado em 3 a 6 vezes (20% de juros""")
print("+---" * 20)
pag = int(input("Escolha uma das formas de pagamento acima: "))
if pag == 4:
    parc = int(input("Escolha o número de parcelas de 3 a 6: "))

if pag == 1:
    print("Você escolheu pagar à vista em dinheiro ou cheque")
    print("O produto irá custar R${:.2f}".format(prod - (prod /100 * 10)))
elif pag == 2:
    print("Você escolheu pagar à vista no cartão")
    print("O produto irá custar R${:.2f}".format(prod - (prod /100 * 5)))
elif pag == 3:
    print("Você escolheu pagar parcelado em 2 vezes")
    print("O produto irá custar R${:.2f}".format(prod))
    print("Em 2 parcelas de R${:.2f}".format(prod / 2))
elif pag == 4:
    print("Você escolheu pagar parcelado em {} vezes".format(parc))
    print("O produto irá custar R${:.2f}".format(prod + (prod / 100 * 20)))
    print("Em {} parcelas de R${:.2f}".format(parc, (prod + (prod / 100 * 20)) / parc))


