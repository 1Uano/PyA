#Зверюшка

class Critter(object):
    total = 0
    """Виртуальный питомец"""
    @staticmethod
    def status():
        print("Общее число зверюшек", Critter.total)
    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total +=1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя:' + self.name 
        return ans

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print('Имя зверюшки не может быть пустой строкой')
        else:
            self.__name = new_name
            print('Имя успешно не изменено.')

    def talk(self):
        print("Меня зовут" ,  self.name)

def main():
    print('Создание зверюшек')
    crit1 = Critter("Зверюшка1" , 100000000 , -1000000000)
    crit2 = Critter("Зверюшка2")

    Critter.status()

    crit1.name ="Бобик"
    print('Имя зверушки:' , crit1.name)
    
    crit2.name =""
    print('Имя зверушки:' , crit2.name)

    print(crit1)
    print('Голод: ' + str(crit1.hunger))
    print('Настроение: ' + str(crit1.boredom))
main()