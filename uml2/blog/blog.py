from postagens import Postagem
from datetime import datetime, date

class Blog:
    
    postagens = []

    def __init__(self, nomeBlog: str) -> None:
        self.nomeBlog = nomeBlog

    def adicionarPostagem(self, postagem : Postagem):
        self.postagens.append(postagem)

    def publicarPostagem(self, postagem: Postagem):
        postagem.dataPublica = datetime.now()

        for duplicada in self.postagens:
            if postagem.id == duplicada.id:
                self.postagens.remove(duplicada)

        self.postagens.append(postagem)

    def listarPostagens(self):
        for i in self.postagens:
            if i.dataPublica < datetime.now():
                listarPostagens = [i]
        
        return listarPostagens

    def listarTodasPostagens(self):
        for i in self.postagens:
            listarTudo = [i]

        return listarTudo

    def apagarPostagem(self, postagem: Postagem):
        for i in self.postagens:
            if i.id == postagem.id :
                self.postagens.remove(i)

    def __str__(self):
        return 'Blog: {}\n'.format(self.nomeBlog)

