class Person:
    def __init__(self, name, age):

        self.__name = name

        if age > 0 and age <= 150:
            self.__age = age
        else:
            print('Error -- The age must be in range [1 - 150]')

    def __str__(self):
        return '{}({})'.format(self.__name, self.__age)

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
