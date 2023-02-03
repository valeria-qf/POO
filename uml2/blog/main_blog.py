from blog import Blog
from usuario import Usuario
from postagens import Postagem
from datetime import datetime

usuarior = Usuario(id = 100, nome = 'valeria', login = 'usuario1', senha = '1234')

postagem = Postagem(id = 111, titulo = 'PESSOA DESAPARECIDA EM PDF', texto =  'JOVEM DESAPARECE APÓS SAIDA COM AMIGOS PARA BALADA', dataPublica = datetime(2023, 1, 10), usuario = usuarior)

blog1 = Blog(nomeBlog = 'noticias')

blog1.adicionarPostagem(postagem)
blog1.listarPostagens()
blog1.listarTodasPostagens()
#blog1.apagarPostagem(postagem)

print(postagem)
print(blog1)