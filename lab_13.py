class Animal:

    def __init__(self, newName):
        self.name = newName
        print(f'Родилось животное {self.name}')

    def eat(self):
        print('Намнём')

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def makeNoise(self):
        print(f'{self.name} говорит Гррр')


class Cat(Animal):
    name = ''
    age = 0
    weight = 0

    def __init__(self):
        print(f'Родился кот')
        Animal.__init__(self, self.name)

    def makeNoise(self):
        print(f'{self.name} говорит Мяу')


class Dog(Animal):
    name = ''
    age = 0
    weight = 0

    def __init__(self):
        print('Родилась собака')
        Animal.__init__(self, self.name)

    def makeNoise(self):
        print(f'{self.name} говорит Гав')


obj = Animal('Скот')
print(obj.getName())
obj.setName('Новый скот')
obj.makeNoise()
obj.eat()

print('\n')

obj_cat = Cat()
obj_cat.name = 'Борис'
obj_cat.makeNoise()
obj_cat.eat()

print('\n')

obj_dog = Dog()
obj_dog.name = 'Шарик'
obj_dog.makeNoise()
obj_dog.eat()


class StringVar:
    text = ""

    def __init__(self, newText):
        self.text = newText

    def set(self, newText):
        self.text = newText
        print('Ошибка исправлена')

    def get(self):
        return self.text


print('\n')
myString = StringVar("Пагода")
print(myString.get())
print("В этом слове есть ошибка")
myString.set(input("Введите исправленное слово\n"))
print(myString.get())


class Point:
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def show_pos(self):
        print(f'(x = {self.pos_x} ; y = {self.pos_y})')

    def del_pos(self):
        self.pos_x = 0
        self.pos_y = 0

    def setPosX(self, x):
        self.pos_x = x

    def setPosY(self, y):
        self.pos_y = y

    def setPoint(self, x, y):
        self.pos_x = x
        self.pos_y = y


print('\n')
newPoint = Point(1, 1)
newPoint.show_pos()
newPoint.del_pos()
newPoint.show_pos()
newPoint.setPosX(10)
newPoint.show_pos()
newPoint.setPosY(10)
newPoint.show_pos()
newPoint.setPoint(-1, -1)
newPoint.show_pos()
