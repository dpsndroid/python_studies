#programa que leia 2 notas do aluno e calcule sua média, com mensagem
#abaixo de 5 reprovado, entre 5 e 6.9 recuperação. 7 ou superior aprovado
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media < 5.0:
    print("Sua média foi {:.1f} e você está \033[:31mREPROVADO\033[m".format(media))
elif media >= 5.0 and media <= 6.9:
    print("Sua média foi {:.1f} e voce está em \033[:33mRECUPERAÇÃO\033[m".format(media))
else:
    print("Sua média foi {:.1f} e você está \033[:32mAPROVADO\033[m".format(media))
