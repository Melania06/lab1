#-*- coding: cp1251 -*-

#SINGLETON

class PartyChest:
    _instance = None # один экземпляр

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.gold = 100
            cls._instance.items = []
        return cls._instance

    def add_item(self, item):
        self.items.append(item)

    def spend(self, amount):
        self.gold -= amount

Astarion_chest = PartyChest()
Astarion_chest.add_item("Astarion's dagger")
Shadowheart_chest = PartyChest()
Shadowheart_chest.spend(25)

print(Astarion_chest is Shadowheart_chest) # один ли сундук или нет
print(Shadowheart_chest.items)
print(Astarion_chest.gold)


#FACTORY METHOD

class Tea: # родитель
    time = 0  # сколько минут заваривать

    def drink(self):
        print(f"Чай заваривать {self.time} мин")


# дети (виды чая)
class GreenTea(Tea):
    time = 3


class BlackTea(Tea):
    time = 4


class OolongTea(Tea):
    time = 2


# знает как подать чай, но не знает какой
class TeaMachine: 
    def make_tea(self):  #FACTORY METHOD
        pass  # не знает какой чай подавать

    def serve(self):
        tea = self.make_tea()  # получаем чай, не зная его вида
        tea.drink()


#  машины с конкретным чаем
class GreenTeaMachine(TeaMachine):
    def make_tea(self):
        return GreenTea()


class BlackTeaMachine(TeaMachine):
    def make_tea(self):
        return BlackTea()


class OolongTeaMachine(TeaMachine):
    def make_tea(self):
        return OolongTea()



machine = GreenTeaMachine()
machine.serve()  

machine = BlackTeaMachine()
machine.serve()  

machine = OolongTeaMachine()
machine.serve()  


#ABSTRACT FACTORY

# родитель1 фигурка
class Figure:
    def __init__(self, character, source):
        self.character = character
        self.source = source

    def show(self):
        print(f"Фигурка: {self.character} ({self.source})")


# дети фигурки
class GameFigure(Figure):
    def __init__(self, character):
        super().__init__(character, "игра")


class AnimeFigure(Figure):
    def __init__(self, character):
        super().__init__(character, "аниме")


# родитель2 подставка
class Stand:
    def __init__(self, style):
        self.style = style

    def show(self):
        print(f"Подставка в стиле: {self.style}")


# дети подставки
class GameStand(Stand):
    def __init__(self):
        super().__init__("Дворец Касадора")


class AnimeStand(Stand):
    def __init__(self):
        super().__init__("цветочное поле")


# фабрика умеет делать фигурку и подставку, но не знает какие
class ShopFactory:
    def create_figure(self):
        pass

    def create_stand(self):
        pass


# конкретные фабрики (каждая делает комплект в одном стиле)
class GameFactory(ShopFactory):
    def create_figure(self):
        return GameFigure("Астарион")

    def create_stand(self):
        return GameStand()


class AnimeFactory(ShopFactory):
    def create_figure(self):
        return AnimeFigure("Фрирен")

    def create_stand(self):
        return AnimeStand()



factory = GameFactory()
factory.create_figure().show()  
factory.create_stand().show()  

factory = AnimeFactory()
factory.create_figure().show()  
factory.create_stand().show()  


#BUILDER

# что собираем
class LegoAnimal:
    def __init__(self):
        self.name = ""
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        parts_str = ", ".join(self.parts)
        return f"{self.name}: {parts_str}"


# родитель/ общие шаги 
class LegoBuilder:
    def __init__(self):
        self.animal = LegoAnimal()

    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_tail_or_wings(self):
        pass

    def build_details(self):
        pass

    def get_result(self):
        return self.animal


# дети: конкретные звери
class FoxBuilder(LegoBuilder):
    def build_head(self):
        self.animal.name = "Лиса"
        self.animal.add("рыжая голова с острой мордочкой")

    def build_body(self):
        self.animal.add("рыжее тело с белой грудкой")

    def build_tail_or_wings(self):
        self.animal.add("длинный пушистый хвост с белым концом")

    def build_details(self):
        self.animal.add("два острых уха")


class OwlBuilder(LegoBuilder):
    def build_head(self):
        self.animal.name = "Сова"
        self.animal.add("круглая рыжая голова с большими глазами")

    def build_body(self):
        self.animal.add("округлое тельце с коричневой грудкой")

    def build_tail_or_wings(self):
        self.animal.add("два широких крыла с белыми концами")

    def build_details(self):
        self.animal.add("жёлтый клюв")


class SquirrelBuilder(LegoBuilder):
    def build_head(self):
        self.animal.name = "Белка"
        self.animal.add("маленькая рыжая голова")

    def build_body(self):
        self.animal.add("тонкое тело с белым брюшком")

    def build_tail_or_wings(self):
        self.animal.add("огромный  хвост")

    def build_details(self):
        self.animal.add("ушки с кисточками")



class Instruction: # знает ПОРЯДОК сборки
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.build_head()
        self.builder.build_body()
        self.builder.build_tail_or_wings()
        self.builder.build_details()



builder = FoxBuilder()
Instruction(builder).build()
print(builder.get_result())  

builder = OwlBuilder()
Instruction(builder).build()
print(builder.get_result())  

builder = SquirrelBuilder()
Instruction(builder).build()
print(builder.get_result())  