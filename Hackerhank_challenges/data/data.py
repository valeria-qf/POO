from datetime import date, timedelta, datetime
'''Ciação da classe Data'''
class Data:
    '''quando a data não for inicializada no construtor, é inserida a data de hoje'''
    def __init__(self, dia = date.today().day, mes = date.today().month, ano = date.today().year):

        '''Verificação de datas válidas'''

        if mes > 0 and mes <=12:
            self.__mes =  mes

        if ano > 0:
            self.__ano = ano
        
        if( mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31):
            self.__dia = dia

        elif( mes in (4, 6, 9, 11) and (dia <=30)):
            self.__dia = dia

        elif (mes == 2):
            
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and dia <=29:
                self.__dia = dia

            elif ano % 4 != 0 and ano % 100 == 0 or ano % 400 != 0 and dia <=28:
                self.__dia = dia

            else:
                print('O mês não possui 29 dias')
        else:
            print('Data inválida')

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes

    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano
                
    def bissexto(self):

        '''metodo que verifica se o ano é bissexto'''

        if (self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano % 400 == 0):
            print('Ano bissexto')
        else:
            print('O ano não é bissexto')

    
    def Avanca_data(self):
        self.__add_Avanca_data()
   
    def __add_Avanca_data(self, NovaData = None):
        if NovaData == None:
            NovaData = datetime(self.__ano, self.__mes, self.__dia) + timedelta(days=1)

        self.__dia = NovaData.day
        self.__mes = NovaData.month
        self.__ano = NovaData.year
        
    '''Metodo que retorna a data como string'''
    def __str__(self):
        return ('Data: {}/{}/{}'.format(self.__dia, self.__mes, self.__ano))

    '''Metodo que soma uma data com outra  do mesmo tipo ou soma uma data com um inteiro(dias)'''

    def __add__(self, other):

        if isinstance(other, Data):
            tempo = other.__dia + other.__ano * 365

            for i in range(0, self.__mes - 1):
                if (i == 2):
                    if (self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano % 400 == 0):
                        tempo += 29
                    else:
                        tempo += 28

                elif (self.__mes in (1, 3, 5, 7, 8, 10, 12)):
                    tempo += 31

                elif (self.__mes in (4, 6, 9, 11)):
                    tempo += 30

            NovaData = datetime(self.__ano, self.__mes, self.__dia) + timedelta(days=tempo)

            return Data(NovaData.day, NovaData.month, NovaData.year)

        elif isinstance(other, int):

            NovaData = datetime(self.__ano, self.__mes, self.__dia) + timedelta(days=other)

            return Data(NovaData.day, NovaData.month, NovaData.year)

    def __radd__(self, other):
        return self.__add__(other)