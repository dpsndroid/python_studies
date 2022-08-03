#ler peso e altura e calcule imc. abaixo de 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal. 25 a 30 sobrepeso. 30 a 40 obesidade.
#acima de 40 obesidade mórbida
peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2
if imc < 18.5:
    print("Seu IMC é {:.1f} e você está \033[1:31mABAIXO DO PESO\033[m".format(imc))
elif imc >= 18.5 and imc <= 25:
    print("Seu IMC é {:.1f} e você está no \033[1:32mPESO IDEAL\033[m".format(imc))
elif imc > 25 and imc <= 30:
    print("Seu IMC é {:.1f} e você está com \033[1:33mSOBREPESO\033[m".format(imc))
elif imc > 30 and imc <= 40:
    print("Seu IMC é {:.1f} e você está com \033[1:31mOBESIDADE\033[m".format(imc))
elif imc > 40:
    print("Seu IMC é {:.1f} e você está com \033[1:31mOBESIDADE MÓRBIDA\033[m".format(imc))