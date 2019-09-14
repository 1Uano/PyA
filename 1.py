#Зверюшка

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя:' + self.name + '\n'
        return ans

    def talk(self):
        print("Меня зовут" ,  self.name)

def main():
    crit1 = Critter("Бобик")
    crit1.talk()
    crit2 = Critter("Мурзик")
    crit2.talk()
    print(crit2)
main()