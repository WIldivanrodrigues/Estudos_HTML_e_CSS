#Obtenha dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:

#- A maior e a menor altura do grupo;
#- A média de altura das pessoas do gênero Masculino;
#- O número de pessoas do gênero Feminino.


pesquisa = [{"altura": 1.75, "genero":"masculino" },
            {"altura": 1.55, "genero":"femenino" },
            {"altura": 1.70, "genero":"masculino" },
            {"altura": 1.88, "genero":"masculino" },
            {"altura": 1.60, "genero":"masculino" },
            {"altura": 1.52, "genero":"femenino" },
            {"altura": 1.79, "genero":"masculino" },
            {"altura": 1.59, "genero":"femenino" },
            {"altura": 1.72, "genero":"masculino" },
            {"altura": 1.83, "genero":"masculino" },
            {"altura": 1.57, "genero":"femenino" },
            {"altura": 1.58, "genero":"masculino" },
            {"altura": 1.70, "genero":"masculino" },
            {"altura": 1.52, "genero":"femenino" },
            {"altura": 1.93, "genero":"masculino" },
            {"altura": 1.62, "genero":"femenino" },
            ]

alturas = [pessoas ["altura"] for pessoas in pesquisa]
maior_altura = max(alturas)
menor_altura = min(alturas)


masculinos = [pessoas ["altura"] for pessoas in pesquisa if pessoas["genero"] == "masculino"]
 
media_alt_masculina = sum(masculinos) / len(masculinos) if masculinos else 0

femenino = len([pessoas for pessoas in pesquisa if pessoas["genero"] == "femenino"])




print(f"De acordo com a pesquisa realizada, a maior altura foi {maior_altura:.2f} metros.")
print(f"De acordo com a pesquisa realizada, a menor altura foi {menor_altura:.2f} metros.")
print(f"De acordo com a pesquisa realizada, a média de altura masculina é de {media_alt_masculina:.2f} metros.")
print(f"de acordo com a pesquisa a quantidade de pessoas do gênero femenino são {femenino} pessoas neste grupo.")
print("Fim de pesquisa!")




