#Programa de cadastro de clientes para analise de emprestimo

#Classe contendo todos os dados do cliente
class Clientedados():
    nome = ""
    cpf = ""
    endereco = ""
    telefone = 0
    renda = 0.0
    direitodeemprestimo = 0.0
    valoremprestimo = 0.0
    banco = ""

#Classe principal que vai realizar todas as operações
class Corpo(Clientedados):

    #Primeira opção do menu que será reponsável por realizar o cadastro
    def cadastro(self):
        print("\n======MENU DE CADASTRO======\n")
        cliente.nome = str(input("Insira o nome completo do cliente: "))
        cliente.cpf = str(input("Insira o CPF do cliente (Ex.: 000.000.000-00): "))
        cliente.endereco = str(input("Insira o endereço do cliente, incluindo número: "))
        cliente.telefone = int(input("Insira o telefone do cliente: "))
        cliente.renda = int(input("Insira a renda mensal do cliente: "))
        #Calculo realizado para saber quanto de empréstimo o cliente poderá realizar
        cliente.direitoemprestimo = (cliente.renda*0.35)/0.02379
        print("\n CADASTRO REALIZADO COM SUCESSO! \n")
        #Chamada de função para retornar ao menu principal, alternativa para o programa ficar sempre rodando e só fechar quando o cliente selecionar a função
        inicio.menu()
 
    #Segunda opção do menu, serve para fazer empréstimo
    def fazeremprestimo(self):
        print("\n======FAZER EMPRESTIMO======\n")
        checacliente = str(input("Insira o nome do cliente: "))

        #Checagem para saber se o cliente digitado existe dentro de cliente.nome
        if checacliente in cliente.nome:
            cliente.banco = str(input("Insira o banco que deseja fazer empréstimo: "))
            #Nessa parte tive que pesquisar melhor como colocar para mostrar apenas um número limitado de casas decimais
            print(f"\nO cliente tem direito a um empréstimo até de: {cliente.direitoemprestimo:.2f} reais.") 
            cliente.valoremprestimo = float(input("Insira o valor do emprestimo: "))
            print("\n EMPRÉSTIMO REALIZADO COM SUCESSO! \n")
            inicio.menu()

        #Caso o cliente não exista o funcionário será direcionado ao menu de realizar empréstimo novamente
        else:
            print("\nNOME NÃO ENCONTRADO, POR FAVOR TENTE NOVAMENTE!\n")
            inicio.fazeremprestimo()

    #Terceira opção do menu, vai realizar uma consulta no nome de algum cliente para saber todos os dados
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

            #Esse "IF" é de muita importancia para mostrar se o cliente possui emprestimo e se possui exibe valor e qual banco foi realizado
            if cliente.valoremprestimo > 0:
                print("Valor do empréstimo: ", cliente.valoremprestimo)
                print("Banco do empréstimo: ", cliente.banco)
            else:
                print("O cliente não tem empréstimo ativo.")
            inicio.menu()
        
        else:
            print("\nNOME NÃO ENCONTRADO, POR FAVOR TENTE NOVAMENTE!\n")
            inicio.consulta()
    
    #Essa função é o coração do programa, pois nele contém o menu que direciona o funcionário a função que deseja
    def menu(self):
        print("\n======MENU DE EMPRESTIMOS======\n")
        print("1. CADASTRAR SITUAÇÃO")
        print("2. FAZER UM EMPRESTIMO")
        print("3. CONSULTAR NOME")
        print("4. FECHAR O PROGRAMA")

        opcao = input("INSIRA A OPÇÃO CORRESPONDENTE: ")

        #Checagem utilizando o "if" para direcionamento do usuário
        if opcao == "1":
            inicio.cadastro()

        elif opcao == "2":
            inicio.fazeremprestimo()

        elif opcao == "3":
            inicio.consulta()
        
        #Opção de encerramento do programa, não direciona a nenhuma função apenas exibe a mensagem de encerrando
        elif opcao == "4":
            print("\nENCERRANDO! \n")

        else:
            print("\nRESPONSTA INCORRETA, POR FAVOR TENTE NOVAMENTE! \n")
            inicio.menu()
    
#Chamada das classes e direcionando o programa para iniciar na função inicio.menu
cliente = Clientedados()
inicio = Corpo()
inicio.menu()