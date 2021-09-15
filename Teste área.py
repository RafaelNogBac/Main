Largura_Garagem = float(input("Largura da Garagem (m): "))
Profundidade_Garagem = float(input("Profundidade da Garagem (m): "))

#calculo da área da garagem
Area_Garagem = Largura_Garagem*Profundidade_Garagem

Largura_Terreno = float(input("Largura do Terreno (m): "))
Profundidade_Terreno = float(input("Profundidade do Terreno (m): "))

#calculo da área do terreno
Area_Terreno = Largura_Terreno*Profundidade_Terreno

#calculo do percentual de ocupação
Percentual = ((Area_Garagem)/(Area_Terreno))* 100

#entrada da zona de localização do terreno
Zona = input("Coloque a localização do terreno aqui: Sul=S, Norte=N, Leste=L, Oeste=O : ")

 #relatorios e mensagens
print("Imóvel localizado na zona: ", Zona)
print("Percentual de ocupação: ", Percentual)

#tomada de decisões
if  Zona == "N" and Percentual <=25:
        print("Projeto atende a norma de zoneamento do plano diretor")
elif Zona == "L" or Zona == "O" and Percentual <=30:
        print("Projeto atende a norma de zoneamento do plano direto")
elif Zona == "S"and Percentual <=40:
        print("Projeto atende a norma de zoneamento do plano direto")
else:
    print("REVISE AS MEDIDAS! Elas não atendem as normas de zoneamento")