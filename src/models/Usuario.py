class Usuario:
    def __init__(self, username, senha, tipo):
        self._username = username
        self._senha = senha
        self._tipo = tipo

    def autenticar(self, username, senha):
        return self._username == username and self._senha == senha

    def possui_permissao_total(self):
        return self._tipo.lower() == "administrador"