"""******************************************************************************************
Autor: Sayumi Mizogami Santana
Componente Curricular: Algoritmos I
Concluido em: 03/09/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************"""
contadorConsultas = 0

#Contagem da quantidade de vezes que cada posto teve o menor preço
qtdMenorPreco_Posto1 = 0
qtdMenorPreco_Posto2 = 0
qtdMenorPreco_Posto3 = 0

#Soma dos litros consultados para tirar a média depois
somaConsultadoPosto1 = 0
somaConsultadoPosto2 = 0
somaConsultadoPosto3 = 0

#Média dos litros consultados
mediaLitrosCons_posto1 = 0
mediaLitrosCons_posto2 = 0
mediaLitrosCons_posto3 = 0

print("----------------------------------------------------------------------------------------")
print("                                  CADASTRO DOS POSTOS                                   ")
print("----------------------------------------------------------------------------------------")

"""nomePosto1 = input("Digite o nome do primeiro posto: ")
gasolinaPreco1 = float(input(f"Digite o preço da gasolina no posto {nomePosto1}: "))
etanolPreco1 = float(input(f"Digite o preço do etanol no posto {nomePosto1}: "))
dieselPreco1 = float(input(f"Digite o preço do diesel no posto {nomePosto1}: "))
print("\n")

nomePosto2 = input("Digite o nome do segundo posto: ")
gasolinaPreco2 = float(input(f"Digite o preço da gasolina no posto {nomePosto2}: "))
etanolPreco2 = float(input(f"Digite o preço do etanol no posto {nomePosto2}: "))
dieselPreco2 = float(input(f"Digite o preço do diesel no posto {nomePosto2}: "))
print("\n")

nomePosto3 = input("Digite o nome do terceiro posto: ")
gasolinaPreco3 = float(input(f"Digite o preço da gasolina no posto {nomePosto3}: "))
etanolPreco3 = float(input(f"Digite o preço do etanol no posto {nomePosto3}: "))
dieselPreco3 = float(input(f"Digite o preço do diesel no posto {nomePosto3}: "))
print("\n")"""

#Isso aqui é só para teste
nomePosto1 = "Posto1"
nomePosto2 = "Posto2"
nomePosto3 = "Posto3"

gasolinaPreco1 = 2
etanolPreco1 = 3
dieselPreco1 = 6

gasolinaPreco2 = 6
etanolPreco2 = 2
dieselPreco2 = 4

gasolinaPreco3 = 10
etanolPreco3 = 6
dieselPreco3 = 3

opcao = "0"
while opcao != "5":
    print("----------------------------------------------------------------------------------------")
    print("                                          MENU                                          ")
    print("----------------------------------------------------------------------------------------")
    print(" 1 - Para inserir o combustível e a litragem desejada")
    print(" 2 - Para mostrar os dados da pesquisa e o posto com o combustível com menor preço")
    print(" 3 - Para listar todos os postos e suas respectivas informações")
    print(" 4 - Para exibir o relatório")
    print(" 5 - Para sair")
    print("----------------------------------------------------------------------------------------")
    opcao = str(input("Digite a opção que deseja seguir: "))
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
            print("ERRO! Digite apenas de 1 a 5!")
            opcao = str(input("Digite a opção que deseja seguir: "))
        
    #OPÇÃO 1
    if opcao == "1":
        contadorConsultas += 1
        tipoCombustivel = str(input("Digite a sua escolha de combustível [Gasolina(1), Etanol(2) ou Diesel(3)]: "))

        #Não permite que o usuário digite nada além dos números 1, 2 e 3
        while tipoCombustivel != "1" and tipoCombustivel != "2" and tipoCombustivel != "3":
            if tipoCombustivel != "1" and tipoCombustivel != "2" and tipoCombustivel != "3":
                print("ERRO!\nExistem apenas 3 tipos de combustíveis no sistema, por favor digite apenas de 1 a 3!")
                tipoCombustivel = str(input("Digite a sua escolha de combustível [Gasolina(1), Etanol(2) ou Diesel(3)]: "))

        #Input da litragem e while para permitir apenas números positivos
        litragem = float(input("Informe a litragem desejada: "))
        while litragem <= 0:
            if litragem <= 0:
                print("ERRO! Digite números positivos!")
            litragem = float(input("Informe a litragem desejada: "))

        #Soma da litragem de cada um e preço total de cada combustível
        if tipoCombustivel == "1":
            nomeDoCombustivel = "Gasolina"
            precoGastoPosto1 = gasolinaPreco1 * litragem
            precoGastoPosto2 = gasolinaPreco2 * litragem
            precoGastoPosto3 = gasolinaPreco3 * litragem

        elif tipoCombustivel == "2":
            nomeDoCombustivel = "Etanol"
            precoGastoPosto1 = etanolPreco1 * litragem
            precoGastoPosto2 = etanolPreco2 * litragem
            precoGastoPosto3 = etanolPreco3 * litragem

        elif tipoCombustivel == "3":
            nomeDoCombustivel = "Diesel"
            precoGastoPosto1 = dieselPreco1 * litragem
            precoGastoPosto2 = dieselPreco2 * litragem
            precoGastoPosto3 = dieselPreco3 * litragem

        print("-------------------------------------------------------------")
        print(f"Valor a ser gasto com o combustível desejado em cada posto: ")
        print(f"Posto {nomePosto1} é: R${precoGastoPosto1:.2f}")
        print(f"Posto {nomePosto2} é: R${precoGastoPosto2:.2f}")
        print(f"Posto {nomePosto3} é: R${precoGastoPosto3:.2f}")
        print("----------------------------------------------------------------------------------------")
        
        #Menor preço que o cliente irá gastar 
        menorPrecoCombustivel = precoGastoPosto1

        if precoGastoPosto2 < menorPrecoCombustivel and precoGastoPosto2 < precoGastoPosto3:
            menorPrecoCombustivel = precoGastoPosto2
            print(f"O menor preço de combustível escolhido é do posto {nomePosto2}, com o gasto total de R${menorPrecoCombustivel}")
            somaConsultadoPosto2 += litragem

        elif precoGastoPosto3 < menorPrecoCombustivel and precoGastoPosto3 < precoGastoPosto2:
            menorPrecoCombustivel = precoGastoPosto3
            print(f"O menor preço de combustível escolhido é do posto {nomePosto3}, com o gasto total de R${menorPrecoCombustivel}")
            somaConsultadoPosto3 += litragem
        
        if menorPrecoCombustivel == precoGastoPosto1:
            print(f"O menor preço de combustível escolhido é do posto {nomePosto1}, com o gasto total de R${menorPrecoCombustivel}")
            somaConsultadoPosto1 += litragem

        #Maior preço que o cliente irá gastar
        maiorPrecoCombustivel = precoGastoPosto1
        
        if precoGastoPosto2 > maiorPrecoCombustivel and precoGastoPosto2 > precoGastoPosto3:
            maiorPrecoCombustivel = precoGastoPosto2
            print(f"O maior preço de combustível é do posto {nomePosto2}, com o gasto total de R${maiorPrecoCombustivel}")

        elif precoGastoPosto3 > maiorPrecoCombustivel and precoGastoPosto3 > precoGastoPosto2:
            maiorPrecoCombustivel = precoGastoPosto3
            print(f"O maior preço de combustível é do posto {nomePosto3}, com o gasto total de R${maiorPrecoCombustivel}")

        if maiorPrecoCombustivel == precoGastoPosto1:
            print(f"O maior preço de combustível é do posto {nomePosto1}, com o gasto total de R${maiorPrecoCombustivel}")
        
        economizou = maiorPrecoCombustivel - menorPrecoCombustivel
        print(f"Valor a ser economizado caso a escolha seja o posto com o menor preço: R${economizou}\n")
        
        #MENORES PREÇOS DOS POSTOS 
        #Menor valor de gasolina
        menorValorGasolina = gasolinaPreco1
        postoGasolinaMenor = nomePosto1

        if gasolinaPreco2 < menorValorGasolina and gasolinaPreco2 < gasolinaPreco3:
            menorValorGasolina = gasolinaPreco2
            postoGasolinaMenor = nomePosto2

        elif gasolinaPreco3 < menorValorGasolina and gasolinaPreco3 < gasolinaPreco2:
            menorValorGasolina = gasolinaPreco3
            postoGasolinaMenor = nomePosto3

        #Menor valor etanol 
        menorValorEtanol = etanolPreco1
        postoEtanolMenor = nomePosto1

        if etanolPreco2 < menorValorEtanol and etanolPreco2 < etanolPreco3:
            menorValorEtanol = etanolPreco2
            postoEtanolMenor = nomePosto2

        elif etanolPreco3 < menorValorEtanol and etanolPreco3 < etanolPreco2:
            menorValorEtanol = etanolPreco3
            postoEtanolMenor = nomePosto3

        #Menor valor diesel 
        menorValorDiesel = dieselPreco1
        postoDieselMenor = nomePosto1

        if dieselPreco2 < menorValorDiesel and dieselPreco2 < dieselPreco3:
            menorValorDiesel = dieselPreco2
            postoDieselMenor = nomePosto2

        elif dieselPreco3 < menorValorDiesel and dieselPreco3 < dieselPreco2:
            menorValorDiesel = dieselPreco3
            postoDieselMenor = nomePosto3
        
        #Contagem de vezes que os postos tiveram o menor preço
        if tipoCombustivel == "1":
            if menorValorGasolina == gasolinaPreco1:
                qtdMenorPreco_Posto1 += 1

            elif menorValorGasolina == gasolinaPreco2:
                qtdMenorPreco_Posto2 += 1

            elif menorValorGasolina == gasolinaPreco3: 
                qtdMenorPreco_Posto3 += 1

        elif tipoCombustivel == "2": 
            if menorValorEtanol == etanolPreco1:
                qtdMenorPreco_Posto1 += 1

            elif menorValorEtanol == etanolPreco2:
                qtdMenorPreco_Posto2 += 1

            elif menorValorEtanol == etanolPreco3:
                qtdMenorPreco_Posto3 += 1

        elif tipoCombustivel == "3":
            if menorValorDiesel == dieselPreco1:
                qtdMenorPreco_Posto1 += 1

            elif menorValorDiesel == dieselPreco2:
                qtdMenorPreco_Posto2 += 1

            elif menorValorDiesel == dieselPreco3:
                qtdMenorPreco_Posto3 += 1

        #CÁLCULO DA MÉDIA DE LITROS CONSULTADOS:
        if contadorConsultas > 0: 
            if qtdMenorPreco_Posto1 > 0: 
                mediaLitrosCons_posto1 = somaConsultadoPosto1 / qtdMenorPreco_Posto1
            else: 
                mediaLitrosCons_posto1 = 0
            
            if qtdMenorPreco_Posto2 > 0:
                mediaLitrosCons_posto2 = somaConsultadoPosto2 / qtdMenorPreco_Posto2
            else:
                mediaLitrosCons_posto2 = 0
            
            if qtdMenorPreco_Posto3 > 0:
                mediaLitrosCons_posto3 = somaConsultadoPosto3 / qtdMenorPreco_Posto3
            else:
                mediaLitrosCons_posto3 = 0

            #MAIORES PREÇOS DOS POSTOS
            #Maior valor de gasolina
            maiorValorGasolina = gasolinaPreco1
            postoGasolinaMaior = nomePosto1

            if gasolinaPreco2 > maiorValorGasolina and gasolinaPreco2 > gasolinaPreco3:
                maiorValorGasolina = gasolinaPreco2
                postoGasolinaMaior = nomePosto2

            if gasolinaPreco3 > maiorValorGasolina and gasolinaPreco3 > gasolinaPreco2:
                maiorValorGasolina = gasolinaPreco3
                postoGasolinaMaior = nomePosto3
                
            #Maior valor etanol
            maiorValorEtanol = etanolPreco1
            postoEtanolMaior = nomePosto1

            if etanolPreco2 > maiorValorEtanol and etanolPreco2 > etanolPreco3:
                maiorValorEtanol = etanolPreco2
                postoEtanolMaior = nomePosto2

            if etanolPreco3 > maiorValorEtanol and etanolPreco3 > etanolPreco2:
                maiorValorEtanol = etanolPreco3
                postoEtanolMaior = nomePosto3

            #Maior valor diesel
            maiorValorDiesel = dieselPreco1
            postoDieselMaior = nomePosto1

            if dieselPreco2 > maiorValorDiesel and dieselPreco2 > dieselPreco3:
                maiorValorDiesel = dieselPreco2
                postoDieselMaior = nomePosto2

            if dieselPreco3 > maiorValorDiesel and dieselPreco3 > dieselPreco2:
                maiorValorDiesel = dieselPreco3
                postoDieselMaior = nomePosto3

    #OPÇÃO 2
    elif opcao == "2":
        if contadorConsultas == 0:
            print("ERRO! Não há dados disponíveis nesse momento! \nTente inserir as informações inicialmente!")
            print("Para inserir os dados, digite 1 no menu e siga as intruções.\n")
            
        else:
            print("\n----------------------------------------------------------------")
            print("Informações da última pesquisa realizada ")
            print("----------------------------------------------------------------")
            print(f"Tipo de combustível escolhido: {nomeDoCombustivel}")
            print(f"Litragem do combustível escolhido: {litragem} litros")
            if tipoCombustivel == "1":
                print(f"Menor valor do combustível escolhido é de R${menorValorGasolina:.2f} no posto {postoGasolinaMenor}")
            elif tipoCombustivel == "2": 
                print(f"Menor valor do combustível escolhido é de: R${menorValorEtanol:.2f} no posto {postoEtanolMenor}")
            elif tipoCombustivel == "3":
                print(f"Menor valor do combustível escolhido é de: R${menorValorDiesel:.2f} no posto {postoDieselMenor}\n")


    #OPÇÃO 3
    elif opcao == "3":
        print("\n-------------------------")
        print(f"Posto {nomePosto1}")
        print("-------------------------")
        print(f"Preços do posto {nomePosto1}")
        print("-------------------------")
        print(f"Gasolina: R${gasolinaPreco1}")
        print(f"Etanol: R${etanolPreco1}")
        print(f"Diesel: R${dieselPreco1}")
 
        print("-------------------------")
        print(f"Posto {nomePosto2}")
        print("-------------------------")
        print(f"Preços do posto {nomePosto2}")
        print("-------------------------")
        print(f"Gasolina: R${gasolinaPreco2}")
        print(f"Etanol: R${etanolPreco2}")
        print(f"Diesel: R${dieselPreco2}")

        print("\n-------------------------")
        print(f"Posto {nomePosto3}")
        print("-------------------------")
        print(f"Preços do posto {nomePosto3}")
        print("-------------------------")
        print(f"Gasolina: R${gasolinaPreco3}")
        print(f"Etanol: R${etanolPreco3}")
        print(f"Diesel: R${dieselPreco3}\n")

    elif opcao == "4":
        if contadorConsultas == 0:
            print("ERRO! Não há dados disponíveis nesse momento! \nTente inserir as informações inicialmente!")
            print("Para inserir os dados, digite 1 no menu e siga as intruções.\n")
            
        else:
            print("-------------------------------------------------------")
            print("RELATÓRIO")
            print("-------------------------------------------------------")
            print(f"Quantidade de consultas realizadas: {contadorConsultas}")
            print(f"Quantidade de vezes que cada posto teve o menor preço: ")
            print(f"{nomePosto1}: {qtdMenorPreco_Posto1}")
            print(f"{nomePosto2}: {qtdMenorPreco_Posto2}")
            print(f"{nomePosto3}: {qtdMenorPreco_Posto3}\n")
            print("-------------------------------------------------------")
            
            print("Média de litros consultados por posto")
            print("-------------------------------------------------------")
            print(f"Posto {nomePosto1}: {mediaLitrosCons_posto1:.1f} litros")
            print(f"Posto {nomePosto2}: {mediaLitrosCons_posto2:.1f} litros")
            print(f"Posto {nomePosto3}: {mediaLitrosCons_posto3:.1f} litros\n")
            print("-------------------------------------------------------")

            print("Relação de preços")
            print("-------------------------------------------------------")
            print(f"GASOLINA\nMenor preço: R${menorValorGasolina:.2f} no posto {postoGasolinaMenor}\nMaior preço: R${maiorValorGasolina:.2f} no posto {postoGasolinaMaior}")
            print("-------------------------------------------------------")
            print(f"ETANOL\nMenor preço: R${menorValorEtanol:.2f} no posto {postoEtanolMenor}\nMaior preço: R${maiorValorEtanol:.2f} no posto {postoEtanolMaior}")
            print("-------------------------------------------------------")
            print(f"DIESEL\nMenor preço: R${menorValorDiesel:.2f} no posto {postoDieselMenor}\nMaior preço: R${maiorValorDiesel:.2f} no posto {postoDieselMaior}\n")

    elif opcao == "5":
        print("----------------------------------------------------------------------------------------")

    else:
        print("ERRO! Digite apenas números de 1 a 5!\n")
        
if opcao != "5":
    limpar = input("Deseja limpar a tela? [S/N]: ")
    if limpar == "S" or limpar == "s":
        print('\033c', end='') #Para limpar tela caso o usuário deseje"

if contadorConsultas != 0:
    print("RELATÓRIO FINAL")
    print("-----------------------------------------")
    print(f"Quantidade de consultas realizadas: {contadorConsultas}")
    print(f"Quantidade de vezes que cada posto teve o menor preço: ")
    print(f"{nomePosto1}: {qtdMenorPreco_Posto1}")
    print(f"{nomePosto2}: {qtdMenorPreco_Posto2}")
    print(f"{nomePosto3}: {qtdMenorPreco_Posto3}")
    print("-------------------------------------")

    print("Média de litros consultados por posto: ")
    print(f"Posto {nomePosto1}: {mediaLitrosCons_posto1:.2f}")
    print(f"Posto {nomePosto2}: {mediaLitrosCons_posto2:.2f}")
    print(f"Posto {nomePosto3}: {mediaLitrosCons_posto3:.2f}")
    print("-------------------------------------------------")

    print("Relação de preços")
    print("-------------------------------------------------")
    print(f"GASOLINA\nMenor preço: R${menorValorGasolina:.2f} no posto {postoGasolinaMenor}\nMaior preço: R${maiorValorGasolina:.2f} no posto {postoGasolinaMaior}")
    print("-------------------------------------------------")
    print(f"ETANOL\nMenor preço: R${menorValorEtanol:.2f} no posto {postoEtanolMenor}\nMaior preço: R${maiorValorEtanol:.2f} no posto {postoEtanolMaior}")
    print("-------------------------------------------------")
    print(f"DIESEL\nMenor preço: R${menorValorDiesel:.2f} no posto {postoDieselMenor}\nMaior preço: R${maiorValorDiesel:.2f} no posto {postoDieselMaior}")
    print("-------------------------------------------------")
else:
    print("Encerrando sem a realização da pesquisa\n")