#Зверюшка

class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет я твоя зверюшка")

def main():
    crit = Critter()
    crit.talk()

main()