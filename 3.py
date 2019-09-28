crits={}

class Critter(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        ans += 'все атрибутты: ' + str(self.boredom) + " " + str(self.hunger) + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("Меня зовут", self.name)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 0):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 0):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def menu(self):
        choice = None  
        while choice != "0":
            print \
            ("""
            Моя зверюшка
    
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """)
    
            choice = input("Ваш выбор: ")
            print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        
        # кормление зверюшки
        elif choice == "2":
            food = int(input('Сколько мне скушать?'))
            crit.eat(food)
         
        # игра со зверюшкой
        elif choice == "3":
            fun = int(input('Ну и сколько мы будем гулять'))
            crit.play(fun)
        
        # секрет
        elif choice == "4":
            print(crit)

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

def main():

    choice2 = None  
    while choice2 != "0":
        print \
        ("""
        ////////////////////////////////
        ////    Создание зверюшки   ////
        ////                        ////
        ////    0 - Выйти           ////
        ////    1 - Создать         ////
        ////    2 - Удалить         ////
        ////    3 - Работа          ////
        ////////////////////////////////
        """)

        choice2 = input("Ваш выбор: ")
        print()

         # выход
        if choice2 == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice2 == "1":
            print('Введите имя зверяяяя')
            name = input()
            pet = Critter(name)
            crits[name] = pet
            
        # кормление зверюшки
        elif choice2 == "2":
            print('Какую зверюшку удалить: ')
            name = input()
            if name in crits:
                del crits[name]
            else:
                print('У нас таких нет!!!!')

        elif choice2 == "3":
            crit.menu()
        
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice2)

    
    
main()