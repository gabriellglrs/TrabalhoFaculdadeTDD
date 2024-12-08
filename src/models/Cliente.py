class Cliente:
    # Inicializa os atributos da classe Cliente.
    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._historico_compras = []  # Lista de compras realizadas

    # Registra uma compra no histórico.
    def registrar_compra(self, compra):
        self._historico_compras.append(compra)

    # Retorna o histórico de compras.
    def obter_historico_compras(self):
        return self._historico_compras