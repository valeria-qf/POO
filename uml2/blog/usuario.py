class Usuario:
    def __init__(self, id: int, nome: str, login: str, senha: str):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha

    def __str__(self) -> str:
        return 'ID: {} \nNome: {} \nLogin: {} \nSenha: {}\n'.format(self.id, self.login, self.nome, self.senha)


