def shellSort(vetor):
    # iniciando com incremento 'incr' razoavelmente grande
    # o 'incr' será decrementado dentro do 'while'
    incr = len(vetor) // 2
    # inserindo elementos de acordo com o incremento
    while incr > 0:
        for i in range(incr, len(vetor)):
            temp = vetor[i]
            j = i
            # ordenando o subvetor relativo ao incremento
            while j >= incr and vetor[j - incr] > temp:
                vetor[j] = vetor[j - incr]
                j = j - incr
            #inserindo o elemento 'temp' na posição certa
            vetor[j] = temp
        # reduzindo o incremento 'incr'
        incr = incr // 2
        
    return vetor
# testando o algoritmo
# substitua os valores de 'vet' para realizar mai testes
vet = [8, 10, 0, 7, 30]
vet_ordenado = shellSort(vet)
print ("result:", vet_ordenado)