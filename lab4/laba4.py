#STRATEGY
class Strategy:
    def attack(self):
        pass
    
class Bow(Strategy):
    def attack(self):
        return 6

class Dagger(Strategy):
    def attack(self):
        return 8

class Spell(Strategy):
    def attack(self):
        return 12

class Character:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_attack(self):
        print(self.strategy.attack())

astarion = Character(Bow())
astarion.make_attack()
astarion.strategy = Dagger()
astarion.make_attack()
astarion.strategy = Spell()
astarion.make_attack()


# RESPONSIBILITY CHAIN
class Request:
    def __init__(self, kind):
        self.kind = kind

# конкретный обработчик 1
class AstarionHandler:
    def __init__(self):
        self.next_handler = None
    def handle(self, request):
        if request.kind == "замок":
            print("Астарион взломал замок")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("Никто не смог справиться")

# конкретный обработчик 2
class GaleHandler:
    def __init__(self):
        self.next_handler = None
    def handle(self, request):
        if request.kind == "магия":
            print("Гейл рассеял магию")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("Никто не смог справиться")

# конкретный обработчик 3
class KarlachHandler:
    def __init__(self):
        self.next_handler = None
    def handle(self, request):
        if request.kind == "сила":
            print("Карлах выбила дверь")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("Никто не смог справиться")

astarion = AstarionHandler()
gale = GaleHandler()
karlach = KarlachHandler()
astarion.next_handler = gale
gale.next_handler = karlach
astarion.handle(Request("замок"))
astarion.handle(Request("магия"))
astarion.handle(Request("сила"))
astarion.handle(Request("лечение"))


# ITERATOR
class Iterator:
    def has_next(self):
        pass
    def next(self):
        pass

class ShelfIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0  # начинаем с 0 тк в питоне начинается с 0 нумерация. оно запоминает позицию
    def has_next(self):
        return self.position < len(self.items) # остались ли элементы
    def next(self):
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        raise IndexError("фигурки закончились")

# коллекция
class FigureShelf:
    def __init__(self):
        self.items = []
    def add(self, figure):
        self.items.append(figure)
    def create_iterator(self):
        return ShelfIterator(self.items)

shelf = FigureShelf()
shelf.add("Астарион")
shelf.add("Фрирен")
shelf.add("Геральт")

iterator = shelf.create_iterator()
while iterator.has_next():
    print(iterator.next())