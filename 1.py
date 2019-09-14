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

    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

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
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'Не ну ты бог'
        elif 5 <= unhappiness <= 100:
            m = 'сойдет'
        else:
            m='Я звоню в ментуру'
        return m

    def talk(self):
        print("Меня зовут" ,  self.name)
        self.__pass_time()

    def eat(self , food = 4):
        print("Мрр.....спасибо")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self , fun = 4):
        print("Хрю")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    print('Создание зверюшек')
    crit1 = Critter("Зверюшка1" , 7 , 7)
    crit2 = Critter("Зверюшка2")

    Critter.status()

    crit1.talk()
    crit1.eat()
    crit1.play()
    print(crit1.mood)

    
    print(crit1)
    print('Голод: ' + str(crit1.hunger))
    print('Усталость: ' + str(crit1.boredom) , '\n')
    
main()