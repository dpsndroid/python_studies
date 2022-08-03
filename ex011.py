alt = float(input("Qual é a altura? "))
base = float(input("Qual é a largura? "))
#litro de tinta pinta 2 metros quadrados
area = base * alt
tinta = area / 2
print("Medidas da parede = {:.2f}m x {:.2f}m".format(base,alt))
print("Área da parede = {:.2f}m²".format(area))
print("Você precisará de {:.1f} litros de tinta".format(tinta))

