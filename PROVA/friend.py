from person import Person

class Friend(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__hobby = hobby

    def get_hobby(self):
        return self.__hobby
    def set_hobby(self, hobby):
        self.__hobby = hobby

    def chill(self):
        return '{} is chilling'.format(self.get_name())

    def play(self, listfriends):
        if len(listfriends) == 0:
            return 'Play {}'.format(self.__hobby)
        elif len(listfriends) == 1: 
            return 'Play {} with {}'.format(self.__hobby, listfriends[0])
        elif len(listfriends) == 2:
            return 'Play {} with {} and {}'.format(self.__hobby, listfriends[0], listfriends[1])
        else:
            msg = 'Play {} with'.format(self.__hobby)
            count = 0
            
            for friend in listfriends:
                if count == len(listfriends) - 1:
                    text += 'and'.format(friend)
                else:
                    text += '{}, '.format(friend)
                    count += 1

            return msg

    def __eq__(self, other):
        if self.get_name() == other.get_name() and self.get_age() == other.get_age() and self.get_hobby() == other.get_hobby():
            return True
        else:
            return False

    def __str__(self):
        return '{}({}) {}'.format(self.get_name(), self.get_age(), self.__hobby.name)