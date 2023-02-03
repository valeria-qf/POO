class Pessoa:
    def __init__(self, name, sexo, data_nasc):
        self.__name = name
        self.__sexo = sexo
        self.__data_nasc =  data_nasc

    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {}'.format(self.__name, self.__sexo, self.__data_nasc)

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def get_data_nasc(self):
        return self.__data_nasc
    def set_data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc
