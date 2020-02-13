from functools import reduce


class Animal:
    satiety = 0

    def __init__(self, weight=0, name=None):
        self.weight = weight
        self.name = name

    def level_of_satiety(self):
        if self.satiety > 0:
            print('Не нужно кормить')
        else:
            print('Нужно покормить')

    def voice(self):
        print(self.voice)

    def __add__(self, other):
        return Animal(self.weight + other.weight)

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight


class Cow(Animal):
    milk = 0
    voice = 'Мууу'

    def get_milk(self):
        if self.milk > 0:
            print('Пора доить!')
        else:
            print('Уже подоили!')

    def get_voice(self):
        print(self.voice)


class Sheep(Animal):
    wool = 0
    voice = 'Беее'

    def get_wool(self):
        if self.wool > 0:
            print('Пора стричь!')
        else:
            print('Уже подстригли!')

    def get_voice(self):
        print(self.voice)


class Goat(Cow):
    milk = 0
    voice = 'Меее'


class Bird(Animal):
    eggs = 0

    def get_eggs(self):
        if self.eggs > 0:
            print('Пора собрать яйца!')
        else:
            print('Уже собрали!')

    def get_voice(self):
        print(self.voice)


class Goose(Bird):
    eggs = 0
    voice = 'Га-га'


class Chicken(Bird):
    eggs = 0
    voice = 'Ко-ко-ко'


class Duck(Bird):
    eggs = 0
    voice = 'Кря-кря'


cow = Cow(500, 'Манька')
sheep_1 = Sheep(50, 'Барашек')
sheep_2 = Sheep(55, 'Кудрявый')
goat_1 = Goat(50, 'Рога')
goat_2 = Goat(55, 'Копыта')
goose_1 = Goose(5, 'Серый')
goose_2 = Goose(8, 'Белый')
chicken_1 = Chicken(1, 'Ко-Ко')
chicken_2 = Bird(2, 'Кукареку')
duck = Duck(2, 'Кряква')

all_animals = [cow, sheep_1, sheep_2, goat_1, goat_2, goose_1, goose_2, chicken_1, chicken_2, duck]

all_weights = reduce(lambda x, y: x + y, all_animals)
print(f'Вес всех животных: {all_weights.weight} кг')

heaviest = reduce(lambda x, y: x if (x > y) else y, all_animals)
print(f'Самое тяжелое животное: {heaviest.name}')
