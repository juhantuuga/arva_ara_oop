"""
Mängu arva ära OOP lahendus. Number sisestatakse tekstina.
Tagaukse sõnaks on "backdoor" ja 10 000 enam ei toimi.
"""
from random import randint


class Model:  # Loome objekti ja anname talle omadused
    def __init__(self):  # __init__ on sisseehitatud meetod; (self) on põhimõtteliselt placeholder
        self.__pc_rand_num = randint(1, 100)  # self viitab iseendale, __ tähendab, et see on privaatne
        self.__steps = 0
        self.__game_over = False
        self.__player_name = ""
        self.__valid_attempt = True  # Petta ei tohi

    #GETTERS - et väline kood (väljaspool classi) saaks muutujaid lugeda, aga mitte neid muuta
    @property
    def pc_rand_num(self):
        return self.__pc_rand_num

    @property
    def steps(self):
        return self.__steps

    @property
    def game_over(self):
        return self.__game_over

    @property
    def player_name(self):
        return self.__player_name

    @property
    def valid_attempt(self):
        return self.__valid_attempt

    #SETTERS - uuendab saadud muutujaid
    @pc_rand_num.setter
    def pc_rand_num(self, value):  # viitab classile ja value on uus väärtus, mis lisatakse
        self.__pc_rand_num = randint(1, 100)

    @steps.setter
    def steps(self, value):
        self.__steps += value

    @game_over.setter
    def game_over(self, value):
        self.__game_over = value

    @player_name.setter
    def player_name(self, value):
        self.__player_name = value

    @valid_attempt.setter
    def valid_attempt(self, value):
        self.__valid_attempt = value

    #STATIC - kuulub classi juurde, aga ei ole classi osa
    @staticmethod
    def is_number(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False

    def ask(self):  # funktsioon ask()
        user_input = input('Sisesta number 1-100: ')  # Väärtustevahemik
        if self.is_number(user_input):
            user_num = int(user_input)  # Peab olema number
            if user_num > self.__pc_rand_num:
                self.__steps += 1
                print('Väiksem')
            elif user_num < self.__pc_rand_num:
                self.__steps += 1
                print('Suurem')
            elif user_num == self.__pc_rand_num:
                self.__steps += 1
                self.__game_over = True  # Mäng läbi, sest arvas ära
                print(f'Juhuu, arvasid ära! Sul läks selleks {self.__steps} sammu. Õige arv oli {self.__pc_rand_num}')
                self.__player_name = input("Sisesta oma nimi: ")  # Küsime kasutaja nime
                if self.__player_name == '':
                    print('Nimetuid edetabelisse ei panda.')  # Anonüümseid sisse ei lasta
                    self.__player_name = input("Sisesta oma nimi: ")
                    if self.__player_name != '':  # Kui enam ei ole tühi, siis
                        self.save_to_file()  # salvestab edetabelisse
                else:
                    self.save_to_file()
        elif user_input.lower() == 'backdoor':
            self.__steps += 1
            print(f'Leidsid tagaukse. Õige number on {self.__pc_rand_num}')
            self.__game_over = False
            self.__valid_attempt = False
        else:
            self.__steps += 1

    def save_to_file(self):
        if self.__valid_attempt:  # Peab olema ausalt teenitud võit
            with open("scoreboard.txt", "a") as file:
                file.write(f"{self.__player_name};{self.__pc_rand_num};{self.__steps}\n")

    def play_again(self):
        answer = input('Kas mängime veel? [J/E] ')
        if answer.lower() == 'j':  # Saab panna ka väikse j ja e, et programm karjuma ei hakkaks
            self.pc_rand_num = randint(1, 100)
            self.__steps = 0
            self.__game_over = False
            self.__valid_attempt = True  # Taastab ka ausa mängu
            return True
        return False


def lets_play():
    model = Model()

    while not model.game_over:
        model.ask()

    if model.play_again():
        lets_play()


if __name__ == '__main__':
    lets_play()
