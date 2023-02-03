from datetime import datetime
from usuario import Usuario

class Postagem:
    def __init__(self, id: int, titulo: str, texto: str, dataPublica: datetime.today(), usuario : Usuario):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.dataPublica = dataPublica
        self.usuario = usuario

    def __str__(self):
        return 'ID: {} \nTitulo: {} \nTexto: {} \ndata de publicação: {} \nUsuario: {}\n'.format(self.id, self.titulo, self.texto,self.dataPublica, self.usuario)

