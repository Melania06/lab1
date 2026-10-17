from abc import ABC, abstractmethod 

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class GameObject:
    def __init__(self, id, name, x, y):
        self._id = id   
        self._name = name  
        self._x = x  
        self._y = y 

    def getId(self): 
        return self._id

    def getName(self):
        return self._name

    def getX(self): 
        return self._x

    def getY(self):  
        return self._y

class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self._hp = hp

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        self._hp= max(0, self._hp - damage)


class Archer(Unit, Attacker, Moveable):
    def __init__(self, id, name, x, y, hp, damage):
        super().__init__(id, name, x, y, hp)
        self._damage = damage
    
    def attack(self, unit):
        unit.receiveDamage(self._damage) 

    def move(self, x, y):
        self._x = x
        self._y = y


class Building(GameObject):
    def __init__(self, id, name, x, y, built=False):
        super().__init__(id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built

class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, damage, built=False):
        super().__init__(id, name, x, y, built)
        self._damage = damage

    def attack(self, unit):
        unit.receiveDamage(self._damage)


class MobileHome(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y









