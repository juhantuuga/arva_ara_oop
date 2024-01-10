"""
Mängu arva ära OOP lahendus. Number sisestatakse tekstina.
Tagaukse sõnaks on "backdoor" ja 10 000 enam ei toimi.
"""
from Model import Model


def lets_play():
    # print(model.pcnr)  # Ütleb õige vastuse
    while not model.game_over:
        model.ask()
    if model.play_again():
        lets_play()
    print('Mäng läbi')


if __name__ == '__main__':
    model = Model()  # Loome mudeli
    lets_play()
