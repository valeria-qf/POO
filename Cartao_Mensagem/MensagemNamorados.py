from cartao_mensagem import CartaoMensagem

class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario)
        self.remetente = remetente

    def __str__(self):
        return (

            'Para {}.\nVocê é a melhor companhia do mundo;\nme provoca múltiplos sorrisos e me encanta\nsempre com palavras lindas. Tenho certeza\nque fomos feitos um para o outro e não há\nninguém melhor que você para passar o resto\nda minha vida. Qualquer momento ao seu lado\n é um tempo bem aproveitado, pois com você sou\nfeliz como nunca fui.\nCom amor, {}\n\n'.format(self.destinatario, self.remetente)  
        )