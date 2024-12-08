import unittest

from src.models.Cliente import Cliente


# Teste para a classe Cliente
class TestCliente(unittest.TestCase):
    # Configuração inicial para os testes.
    def setUp(self):
        self.cliente = Cliente("João Silva", "123.456.789-00", "joao@email.com")

    # Testa se os atributos do cliente foram inicializados corretamente.
    def test_atributos_cliente(self):
        self.assertEqual(self.cliente._nome, "João Silva")
        self.assertEqual(self.cliente._cpf, "123.456.789-00")
        self.assertEqual(self.cliente._email, "joao@email.com")

    # Testa se o registro de compras funciona corretamente.
    def test_registrar_compra(self):
        self.cliente.registrar_compra("Compra de pneus")
        self.assertIn("Compra de pneus", self.cliente.obter_historico_compras())

    # Testa se o histórico de compras é retornado corretamente.
    def test_obter_historico_compras(self):
        self.cliente.registrar_compra("Compra de bateria")
        self.cliente.registrar_compra("Compra de óleo")
        self.assertEqual(self.cliente.obter_historico_compras(), ["Compra de bateria", "Compra de óleo"])

if __name__ == "__main__":
    unittest.main()

