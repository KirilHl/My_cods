class Person: 

    def init(self, name):                      #Конструктор класса          
        self.name = name  # имя человека       #Атрибут
        self.age = 1  # возраст человека
tom = Person()
tom.age = 31
print(tom.age)                                 #Выыод информации из класса

#другой код

while True:
    class Person:
        def say(self, message):
            print(message)


    tom = Person()
    tom.say(input())  # Hello work

#Еще другой коооод

class Person:

    def __init__(self, name):
        self.name = name  # имя человека
        self.age = 1  # возраст человека
        self.company = 5

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age} Company: {self.company}")


tom = Person("Tom")
tom.display_info()
