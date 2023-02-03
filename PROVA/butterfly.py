from insect import Insect

class Butterfly(Insect):
    def __init__(self, species, colors = [], butterfly = None):
        super().__init__(species)
        self.__colors = colors
        self.__butterfly = butterfly

    def get_colors(self):
        return self.__colors
    def set_colors(self, colors):
        self.__colors = colors

    def get_butterfly(self):
        return self.__butterfly
    def set_butterfly(self, butterfly):
        self.__butterfly = butterfly

    def __str__(self):
        return 'Species: {} {}'.format(self.get_species(), self.__colors)