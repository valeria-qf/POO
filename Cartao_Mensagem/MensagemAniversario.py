from cartao_mensagem import CartaoMensagem

class MensagemAniversario(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario)
        self.remetente = remetente

    def __str__(self):
        return (
        'Para {}\nFelicitações!\nQue seu dia seja completo\nde paz, amor e felicidade.\nNão esqueça de sorrir, pois\nsua alegria é contagiante.\nParabéns!\n\nCom amor, {}\n\n'.format(self.destinatario, self.remetente)
        )