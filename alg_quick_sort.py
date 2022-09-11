def divide(vetor, inf, sup):
    # seleção do pivô
    pivo = vetor[inf]
    # particionamento
    esq = inf
    ddir = sup
    
    while esq < ddir:
        # busca o elemento maior que o pivô
        while vetor[esq] <= pivo and esq < sup:
            esq = esq + 1
        # busca o elemento menor que o pivô
        while vetor[ddir] > pivo:
            ddir = ddir - 1
        if esq < ddir:
            # troca as posições dos elementos encontrados
            temp = vetor[esq]
            vetor[esq] = vetor[ddir]
            vetor[ddir] = temp
            
    # coloca o pivô no lugar correto
    vetor[inf] = vetor[ddir]
    vetor[ddir] = pivo
    # ddir é o índice em que o pivô atualmente está
    return ddir
    
def quickSort(vetor, inf, sup):
    if inf >= sup:
        return
    indice_pivo = divide(vetor, inf, sup)
    quickSort(vetor, inf, indice_pivo - 1)
    quickSort(vetor, indice_pivo + 1, sup)
    
def main(vetor):
    n = len(vetor)
    quickSort(vetor, 0, n-1)
    print("\nVetor ordenado:", vetor)
    
# testando o algoritmo
# substitua os valores de 'vet' para realizar mai testes
vet = [3, 50, 40, 10, 30]
pet = [3, 50, 40, 10, 30]
main(vet)
