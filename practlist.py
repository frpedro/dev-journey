renda = []

#  # Pede o saldo de cada fonte de renda soma e mostra os resultados
def pegasaldo():
    fontes = int(input("Quantas fontes de renda vc tem? "))

    try:
        for resposta in range(1, fontes +1 ):
            resposta = int(input("Digite os valores um de cada vez: "))
            renda.append(resposta)
    except:
        print("resposta invalida tente novamente")

    soma = sum(renda)
    print(f"O resultado da lista toda: {renda}")
    print(f"E a soma da lista é: {soma}")

# Ordena por escolha do usuário
def ordenar():
    while True:
        ordenarquest = input("Ordenar por ordem? 'C' para crescente / 'D' para decrescente / 'N' para realizar nenhuma ação ").lower()
        
        if ordenarquest == "c":
            renda.sort()
            print(renda)
            break
        elif ordenarquest == "d":
            renda.sort()
            renda.reverse()
            print(renda)
            break
        elif ordenarquest == "n":
            print("Ok! Nada feito.")
        else:
            print("Opção inválida, tente novamente...")

pegasaldo()
ordenar()