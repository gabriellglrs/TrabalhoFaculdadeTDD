import unittest

from src.models.Usuario import Usuario


class TestUsuario(unittest.TestCase):
    # Configuração inicial para os testes.
    def setUp(self):
        self.usuario_admin = Usuario("admin", "1234", "administrador")
        self.usuario_funcionario = Usuario("funcionario1", "abcd", "funcionario")

    # Testa a autenticação com credenciais corretas.
    def test_autenticar_sucesso(self):
        self.assertTrue(self.usuario_admin.autenticar("admin", "1234"))

    # Testa a autenticação com credenciais incorretas.
    def test_autenticar_falha(self):
        self.assertFalse(self.usuario_admin.autenticar("admin", "senha_errada"))

    # Testa se o administrador possui permissão total.
    def test_possui_permissao_total_admin(self):
        self.assertTrue(self.usuario_admin.possui_permissao_total())

    # Testa se um funcionário não possui permissão total.
    def test_possui_permissao_total_funcionario(self):
        self.assertFalse(self.usuario_funcionario.possui_permissao_total())

if __name__ == "__main__":
    unittest.main()
