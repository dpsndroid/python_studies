class Quadrilatero:
    def __init__(self, lado1, lado2, lado3, lado4):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__lado4 = lado4
    
    def calcula_perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3 + self.__lado4

class Quadrado(Quadrilatero):
    def __init__(self, lado1, lado2, lado3, lado4):
        super().__init__(lado1, lado2, lado3, lado4)

    def verifica_lados_iguais(self):
        if self.__lado1 == self.__lado2 == self.__lado3 == self.__lado4:
            print("Lados iguais")
        else:
            print("Lados diferentes")

quadrado1 = Quadrado(12,12,12,12)
quadrado2 = Quadrado(12,13,12,14)
quadrado1.verifica_lados_iguais()
quadrado2.verifica_lados_iguais()
