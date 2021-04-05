class Clientedados():
    nome = ""
    cpf = ""
    endereco = ""
    telefone = 0
    renda = 0.0
    direitodeemprestimo = 0.0
    valoremprestimo = 0.0
    banco = ""

class Corpo(Clientedados):

    def cadastro(self):
        print("\n======MENU DE CADASTRO======\n")
        cliente.nome = str(input("Insira o nome completo do cliente: "))
        cliente.cpf = str(input("Insira o CPF do cliente (Ex.: 000.000.000-00): "))
        cliente.endereco = str(input("Insira o endereço do cliente, incluindo número: "))
        cliente.telefone = int(input("Insira o telefone do cliente: "))
        cliente.renda = int(input("Insira a renda mensal do cliente: "))
        cliente.direitoemprestimo = (cliente.renda*0.35)/0.02379
        print("\n CADASTRO REALIZADO COM SUCESSO! \n")
        inicio.menu()
 
    def fazeremprestimo(self):
        print("\n======FAZER EMPRESTIMO======\n")
        checacliente = str(input("Insira o nome do cliente: "))

        if checacliente in cliente.nome:
            cliente.banco = str(input("Insira o banco que deseja fazer empréstimo: "))
            print(f"\nO cliente tem direito a um empréstimo até de: {cliente.direitoemprestimo:.2f} reais.")
            cliente.valoremprestimo = float(input("Insira o valor do emprestimo: "))
            print("\n EMPRÉSTIMO REALIZADO COM SUCESSO! \n")
            inicio.menu()

        else:
            print("\nNOME NÃO ENCONTRADO, POR FAVOR TENTE NOVAMENTE!\n")
            inicio.fazeremprestimo()

    def consulta(self):
        print("\n======CONSULTA SITUAÇÃO======\n")
        checacliente = str(input("Insira o nome do cliente: "))

        if checacliente in cliente.nome:
            print("\nDados do cliente: ")
            print("Nome: ", cliente.nome)
            print("CPF: ", cliente.cpf)
            print("Endereço: ", cliente.endereco)
            print("Telefone: ", cliente.telefone)
            print("Renda: ", cliente.renda)
            if cliente.valoremprestimo > 0:
                print("Valor do empréstimo: ", cliente.valoremprestimo)
                print("Banco do empréstimo: ", cliente.banco)
            else:
                print("O cliente não tem empréstimo ativo.")
            inicio.menu()
        
        else:
            print("\nNOME NÃO ENCONTRADO, POR FAVOR TENTE NOVAMENTE!\n")
            inicio.consulta()
        
    def menu(self):
        print("\n======MENU DE EMPRESTIMOS======\n")
        print("1. CADASTRAR SITUAÇÃO")
        print("2. FAZER UM EMPRESTIMO")
        print("3. CONSULTAR NOME")
        print("4. FECHAR O PROGRAMA")

        opcao = input("INSIRA A OPÇÃO CORRESPONDENTE: ")

        if opcao == "1":
            inicio.cadastro()

        elif opcao == "2":
            inicio.fazeremprestimo()

        elif opcao == "3":
            inicio.consulta()
        
        elif opcao == "4":
            print("\nENCERRANDO! \n")

        else:
            print("\nRESPONSTA INCORRETA, POR FAVOR TENTE NOVAMENTE! \n")
            inicio.menu()
    
cliente = Clientedados()
inicio = Corpo()
inicio.menu()