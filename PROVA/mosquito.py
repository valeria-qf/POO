from nuisance import Nuisance
from insect import Insect
class Mosquito(Insect, Nuisance):
    def __init__(self, species):
        super().__init__(species)

    def buzz(self):
        return '{} buzzing around'.format(self.get_species())

    def annoy(self):
        return 'buzz buzz buzz'