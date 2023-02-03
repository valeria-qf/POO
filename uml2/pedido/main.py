from produto import Produto
from itemPedido import ItemPedido
from pedido import Pedido

camisa = Produto(codigo = 10, descricao = 'camisa', valor = 50)
calca = Produto(codigo = 11, descricao = 'calça', valor = 100)
jaqueta = Produto(codigo = 12, descricao = 'jaqueta', valor = 80)

item1 = ItemPedido(camisa, 1)
item2 = ItemPedido(calca, 1)
item3 = ItemPedido(jaqueta, 1)

pedido = Pedido(0)
pedido.adicionarItem(item1)
pedido.adicionarItem(item2)
pedido.adicionarItem(item3)

print(pedido.obterTotal())