#Dicionários
dados = {"nome": "Pedro", "idade": 25}
# ou
#dados1 = dict("nome":"Antonio", "idade":27)

print(dados["nome"])
print(dados["idade"])
dados["sexo"]= "M"
print(dados)
filme = {"titulo": "StarWars",
         "ano": 1977,
         "diretor": "George Lucas",
         "categ": "Ficção"
        }
print(filme) #imprime tudo na ordem de adição, como na lista
print(filme.values()) #imprime os conteúdos
print(filme.keys()) #imprime os títulos para os conteúdos
print(filme.items()) #exibe na mesma ordem de adição, com separação para visualizar
for k,v in filme.items():
    print(f"O {k} é {v}")

pessoas = {"nome": "Daniel", "sexo": "M", "idade": 45}
print(f"Estudante {pessoas['nome']} tem {pessoas['idade']}")
del pessoas["sexo"]
print(pessoas)
pessoas["nome"] = "Eduardo"
print(pessoas)
pessoas["peso"] = 94.5
print(pessoas)

brasil = []
estado1 = {"UF": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"UF": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]["UF"])
print(brasil[1]["sigla"])
estado = {}
for c in range(0,3):
    estado["UF"] = str(input("Estado: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} é {v}.")
