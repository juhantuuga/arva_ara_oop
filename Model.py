from random import randint


class Model:
    # Modeli loomise hetkel seadistatakse mängu algseis.
    def __init__(self):
        self.__pcnr = randint(1, 100)
        self.__steps = 0
        self.__game_over = False

    # GETTERS
    @property
    def pcnr(self):
        return self.__pcnr

    @property
    def steps(self):
        return self.__steps

    @property
    def game_over(self):
        return self.__game_over

    # SETTERS
    @pcnr.setter
    def pcnr(self, value):
        self.__pcnr = randint(1, 100)

    @steps.setter
    def steps(self, value):
        self.__steps += value

    @game_over.setter
    def game_over(self, value):
        self.__game_over = value

    @staticmethod
    def is_number(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False

    def ask(self):
        usernr = input('Sisesta number: ')
        if self.is_number(usernr):
            usernr = int(usernr)
            if usernr > self.__pcnr:
                self.__steps += 1
                print('Väiksem')
            elif usernr < self.__pcnr:
                self.__steps += 1
                print('Suurem')
            elif usernr == self.__pcnr:
                self.__steps += 1
                self.__game_over = True
                print(f'Juhuu, arvasid ära! Sul läks selleks {self.__steps} sammu. Õige arv oli {self.__pcnr}')

        elif usernr == 'backdoor':
            self.__steps += 1
            print(f'Leidsid tagaukse. Õige number on {self.__pcnr}')
        else:
            self.__steps += 1

    def play_again(self):
        answer = input('Kas mängime veel? [J/E] ')
        if answer.upper() == 'J':
            self.pcnr = randint(1, 100)
            self.__steps = 0
            self.__game_over = False
            return True
        return False
