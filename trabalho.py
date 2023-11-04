class Pessoa:
    def __init__(self, nome, cpf, rg, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento


class Cadastrar(Pessoa):
    def cadastrarCliente(self, nome, cpf, rg, dataNascimento, tipoCliente):
        cliente = Cliente(nome, cpf, rg, dataNascimento, tipoCliente)
        return cliente

    def cadastrarGerente(self, nome, cpf, rg, dataNascimento, cargo):
        gerente = Gerente(nome, cpf, rg, dataNascimento, cargo)
        return gerente

    def cadastrarVendedor(self, nome, cpf, rg, dataNascimento, comissão, meta):
        vendedor = Vendedor(nome, cpf, rg, dataNascimento, comissão, meta)
        return vendedor


class Gerente(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, cargo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.cargo = cargo

    def gerarRelatorio(self):
        print("Relatório gerado")

    def consultarCliente(self, cpf):
        cliente = Cadastrar.consultarCliente(cpf)
        return cliente

    def consultarVendedor(self, cpf):
        vendedor = Cadastrar.consultarVendedor(cpf)
        return vendedor


class Cliente(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, tipoCliente):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.tipoCliente = tipoCliente

    def selecionarCompra(self, produtos):
        print("Compra selecionada")

    def fazerCompra(self, valor):
        print("Compra feita")

    def cancelarCompra(self, valor):
        print("Compra cancelada")


class Vendedor(Pessoa):
    def __init__(self, nome, cpf, rg, dataNascimento, comissão, meta):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.comissão = comissão
        self.meta = meta

    def adicionarProduto(self, produto):
        print("Produto adicionado")

    def fazerVenda(self, valor):
        print("Venda feita")

    def gerarRelatorioDeVenda(self):
        print("Relatório de venda gerado")

    def atenderCliente(self):
        print("Cliente atendido")

    def resolverReclamação(self):
        print("Reclamação resolvida")
