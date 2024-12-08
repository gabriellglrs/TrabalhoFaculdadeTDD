import unittest

from src.models.Usuario import Usuario


class TestUsuario(unittest.TestCase):
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.usuario_admin = Usuario("admin", "1234", "administrador")
        self.usuario_funcionario = Usuario("funcionario1", "abcd", "funcionario")

    def test_autenticar_sucesso(self):
        """
        Testa a autenticação com credenciais corretas.
        """
        self.assertTrue(self.usuario_admin.autenticar("admin", "1234"))

    def test_autenticar_falha(self):
        """
        Testa a autenticação com credenciais incorretas.
        """
        self.assertFalse(self.usuario_admin.autenticar("admin", "senha_errada"))

    def test_possui_permissao_total_admin(self):
        """
        Testa se o administrador possui permissão total.
        """
        self.assertTrue(self.usuario_admin.possui_permissao_total())

    def test_possui_permissao_total_funcionario(self):
        """
        Testa se um funcionário não possui permissão total.
        """
        self.assertFalse(self.usuario_funcionario.possui_permissao_total())

if __name__ == "__main__":
    unittest.main()
