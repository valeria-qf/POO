from cartao_mensagem import CartaoMensagem

class MensagemNatal(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario)
        self.remetente = remetente

    def __str__(self):
        return (
            'Para {} e família.\nQue neste Natal o amor e a esperança\naqueçam seus corações e o Ano Novo traga\ngrandes realizações e muita felicidade.\nQue não faltem a boa comida e os ricos\npresentes, mas principalmente que haja\nsaúde, alegria e bons sentimentos para\ncompartilhar. E que cada um de vocês celebre\nestas festas junto da família ou daqueles que\nmais ama. Feliz Natal e um próspero Ano Novo para todos!\n\nCom amor, {} e família\n\n'.format(self.destinatario, self.remetente)
        )