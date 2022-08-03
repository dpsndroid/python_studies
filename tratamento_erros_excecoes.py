print("-" * 20)
print("Primeira opção")
print("-" * 20)
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except:
    print("Infelizmente tivemos um problema :(")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre. Muito obrigado")

print()
print("-" * 20)
print("Segunda opção")
print("-" * 20)
try:
    c = int(input("Numerador: "))
    d = int(input("Denominador: "))
    s = c/d
except Exception as erro:
    print(f"O problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado é {s:.1f}")
finally:
    print("Volte sempre. Muito obrigado")

print()
print("-" * 20)
print("Terceira opção")
print("-" * 20)
try:
    c = int(input("Numerador: "))
    d = int(input("Denominador: "))
    s = c/d
except (ValueError, TypeError):
    print("Tivemos um problema com tipos de dados que você digitou")
except ZeroDivisionError:
    print("Não é possível dividir o número por zero")
except KeyboardInterrupt:
    print("O usuário preferiu não inserir os dados")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {s:.1f}")
finally:
    print("Volte sempre. Muito obrigado")