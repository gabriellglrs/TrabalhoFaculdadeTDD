import unittest

from src.models.Produto import Produto


# Teste para a classe Produto
class TestProduto(unittest.TestCase):

    # Configuração inicial para os testes.
    def setUp(self):
        self.produto = Produto(101, "Goodyear", 50, 200.0)

    # Testa se os atributos do produto foram inicializados corretamente.
    def test_atributos_produto(self):
        self.assertEqual(self.produto._codigo, 101)
        self.assertEqual(self.produto._marca, "Goodyear")
        self.assertEqual(self.produto._quantidade, 50)
        self.assertEqual(self.produto._valor_unitario, 200.0)

    # Testa se o método atualizar_estoque funciona corretamente.
    def test_atualizar_estoque(self):
        self.produto.atualizar_estoque(20)
        self.assertEqual(self.produto._quantidade, 70)

    # Testa se o valor total do estoque é calculado corretamente.
    def test_calcular_valor_total(self):
        self.assertEqual(self.produto.calcular_valor_total(), 10000.0)

if __name__ == "__main__":
    unittest.main()
