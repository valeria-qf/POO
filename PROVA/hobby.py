from enum import Enum
class Hobby(Enum):
    music = 1
    sports = 2
    games = 3

    def print_my_hobby_is_games(hobby):
        if hobby == Hobby.games:
            print('Meu hobby é {}'.format(hobby.name))
        else: 
            print('Meu hobby não é games e sim: {}'.format(hobby.name))
