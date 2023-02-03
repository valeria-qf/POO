import datetime

class Data:
    '''quando a data não for inicializada no construtor, é inserida a data de hoje'''
    def __init__(self, dia = datetime.date().day, mes = datetime.date().month, ano = datetime.date().year):

        if mes > 0 and mes <=12:
            self.__mes = mes

        if ano > 0:
            self.__ano = ano
        
        if dia > 0 and dia <= 31:
            if (self.__mes == 1 or self.__mes == 3 or self.__mes == 5 or self.__mes == 7 \
                or self.__mes == 8  or self.__mes == 10  or self.__mes == 12):
                
                if (self.__dia <= 31):
                    self.__dia = dia
                else:
                    print('O mês não possui 31 dias')

            elif(self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11):

                if(self.__dia <= 30):
                    self.__dia = dia
                else:
                    print('O mês não possui 30 dias')

                '''Se o mes for fevereiro e o ano bissexto, fevereiro terá 29 dias, senão 28'''
            elif (self.__mes == 2):
                if (self.bissexto):
                    if (self.__dia <= 29):
                        self.__dia = dia

                elif (self.__dia <= 28):
                    self.__dia == dia

                else:
                    print('O mês não possui 28/29 dias')
                
    def bissexto(self):
        '''função que verifica se o ano é bissexto'''
        if (self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano % 400 == 0):
            return True
        else:
            return False 

    def Avanca_data(self):
        '''
        Função que avança a data:

        31/12  incrementa ano, dia = 1, mes = 1 (janeiro)
        bissexto dia 29, incrementa mês e dia = 1
        meses com 30 dias incrementa mês e dia = 1
        meses com 31 dias incrementa mês e dia = 1

        '''

        if (self.__dia == 31 and self.__mes == 12):
            self.__ano += 1
            self.__dia = 1
            self.__mes = 1

        elif (self.__dia == 30 and (self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11)): 

            self.__mes += 1
            self.__dia = 1

        elif (self.__dia == 31 and (self.__mes == 1 or self.__mes == 3 or self.__mes == 5 or \
            self.__mes == 7  or self.__mes == 8  or self.__mes == 10  or self.__mes == 12)):

            self.__mes += 1
            self.__dia = 1

        elif (self.__mes == 2):
            if (self.bissexto and self.__dia == 29):
                self.__mes += 1
                self.__dia = 1
            elif (self.__dia == 28):
                self.__mes += 1
                self.__dia = 1
        
    def __str__(self):
        return Data('Data: {}/{}/{}'.format(self.__dia, self.__mes, self.__ano))

data = Data(30, 12, 2020)
d2 = Data()
data.Avanca_data()