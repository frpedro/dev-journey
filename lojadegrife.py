class Pesquisa:
    nike = ("Camisa", "Tenis", "Painters", "Chuteiras", "Caps")
    adidas = ("Camisa", "Tenis", "Painters", "Chuteiras", "Caps")
    golden = ("Camisa", "Tenis", "Painters", "Zip", "Caps")
    versace = ("Camisa", "Tenis", "Painters", "Cinto", "Caps")
    ferrag = ("Camisa", "Tenis", "Painters", "Cinto", "Caps")

    # Função de menu feito para procurar marcas, entregar resultados e validar respostas
    @staticmethod
    def menu():
        while True:
            print("1 - Nike, 2 - Adidas, 3 - GoldenGoose, 4 - Versace, 5 - Ferragamo")
            search = int(input("Qual categoria tá afim de comprar? Digita o número aí: "))
            match search:
                case 1:
                    print("Produtos disponíveis:", Pesquisa.nike)
                    break
                case 2:
                    print("Produtos disponíveis:", Pesquisa.adidas)
                    break
                case 3:
                    print("Produtos disponíveis:", Pesquisa.golden)
                    break
                case 4:
                    print("Produtos disponíveis:", Pesquisa.versace)
                    break
                case 5:
                    print("Produtos disponíveis:", Pesquisa.ferrag)
                    break
                case _:
                    print("Opção inválida, tente novamente...")

# Chama função
Pesquisa.menu()