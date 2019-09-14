#Зверюшка

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась зверюшка")

    def talk(self):
        print("Привет я твой зверюшка")

def main():
    crit1 = Critter()
    crit1.talk()
    crit2 = Critter()
    crit2.talk()
main()