class Date:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def __str__(self):
        return '{}/{}/{}'.format(self.__dia, self.__mes, self.__ano)