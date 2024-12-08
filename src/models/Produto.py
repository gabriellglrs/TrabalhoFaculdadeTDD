class Produto:
    # Inicializa os atributos da classe Produto.
    def __init__(self, codigo, marca, quantidade, valor_unitario):
        self._codigo = codigo
        self._marca = marca
        self._quantidade = quantidade
        self._valor_unitario = valor_unitario

    # Atualiza o estoque do produto.
    def atualizar_estoque(self, quantidade):
       self._quantidade += quantidade

    # Calcula o valor total do estoque.
    def calcular_valor_total(self):
        return self._quantidade * self._valor_unitario