class Pessoa:
    def __init__(self, nome, cpf, rg, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
         

class Gerente(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, cargo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.cargo = cargo

    def gerarRelatorio(self):
        print("Relatório gerado !")

    def consultarCliente(self):
        print("Cliente consultado !")

    def consultarVendedor(self):
         print("Vendedor consultado !")
    
    def cadastrarGerente(self, nome, cpf, rg, dataNascimento, cargo):
        gerente = Gerente(nome, cpf, rg, dataNascimento, cargo)
        return gerente


class Cliente(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, tipoCliente):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.tipoCliente = tipoCliente

    def selecionarCompra(self, produtos):
        print("Compra selecionada !")

    def fazerCompra(self, valor):
        print("Compra feita !")

    def cancelarCompra(self, valor):
        print("Compra cancelada !")

    def cadastrarCliente(self, nome, cpf, rg, dataNascimento, tipoCliente):
        cliente = Cliente(nome, cpf, rg, dataNascimento, tipoCliente)
        return cliente

class Vendedor(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, comissão, meta):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.comissão = comissão
        self.meta = meta

    def adicionarProduto(self, produto):
        print("Produto adicionado !")

    def fazerVenda(self, valor):
        print("Venda feita !")

    def gerarRelatorioDeVenda(self):
        print("Relatório de venda gerado !")

    def atenderCliente(self):
        print("Cliente atendido !")

    def resolverReclamação(self):
        print("Reclamação resolvida !")

    def cadastrarVendedor(self, nome, cpf, rg, dataNascimento, comissão, meta):
        vendedor = Vendedor(nome, cpf, rg, dataNascimento, comissão, meta)
        return vendedor 
    
if __name__ == '__main__':
    opcao = 0
    while opcao != 4:
        print("----= Bem Vindo a Loja de jogos =----")
        print("selecione seu tipo de usuário")
        opcao = int(input("(1)Cliente (2)Vendedor (3)Gerente (4)sair: "))

        if opcao not in [1, 2, 3,4]:
            print("O valor inserido deve estar entre 1 e 4")
            continue

        if opcao == 1: 
            cliente = Cliente("João", "123.456.789-00", "123.456.789-00", "1999-01-01", "Padrão")

            login = (input('Digite o login do Cliente:'))
            senha = (input('Digite a senha do cliente:'))  
            print("Cliente logado !")
            MenuCliente = 0
            while MenuCliente != 4:   
                print("--=Menu do cliente=--") 
                MenuCliente = int(input("(1)Selecionar Compra (2)Fazer Compra (3)Cancelar Compra (4)Sair:"))
                
                if MenuCliente == 1:
                       cliente.selecionarCompra(["Jogo 1", "Jogo 2"])
                if MenuCliente == 2:
                 cliente.fazerCompra(['200'])

                if MenuCliente == 3:
                 cliente.cancelarCompra(['200']) 

        if opcao == 2:      
            Vendedor = Vendedor("marcos", "105.243.299.23", "123.123.123-00", "1999-01-02", "2%", "51%")

            login = (input('Digite o login do Vendedor:'))
            senha = (input('Digite a senha do Vendedor:')) 
            print("Vendedor logado !")   
            MenuVendedor = 0 
            while MenuVendedor != 6:
             print("--=Menu do Vendedor=--")   
             MenuVendedor = int(input("(1)Adicionar Produto (2)Fazer Venda (3)Gerar Relatorio de Venda (4)Atender Cliente (5)Resolver Reclamação (6)Sair:")) 

             if MenuVendedor == 1: 
               Vendedor.adicionarProduto(['jogo de aventura']) 

             if MenuVendedor == 2: 
                Vendedor.fazerVenda(['200'])     

             if MenuVendedor == 3: 
                Vendedor.gerarRelatorioDeVenda()    

             if MenuVendedor == 4:
                Vendedor.atenderCliente()  

             if MenuVendedor == 5: 
                Vendedor.resolverReclamação()    

        if opcao == 3: 
            gerente = Gerente("Lucas","256.709.900-05","27.543.264-6","2000-02-04","Gerente supervisor")

            login = (input('Digite o login do gerente:'))
            senha = (input('Digite a senha do gerente:'))  
            print("Gerente logado !")  

            MenuGerente = 0 
            while MenuGerente != 4:   
             MenuGerente = int(input('(1)Gerar Relatorio (2)Consultar Cliente (3)Consultar Vendedor (4)Sair:'))  

             if MenuGerente == 1: 
                gerente.gerarRelatorio() 

             if MenuGerente == 2: 
                gerente.consultarCliente()  

             if MenuGerente == 3:
                gerente.consultarVendedor() 
      
   
    print("Obrigado por usar nossa loja!")


   

    


            

       


       
        


