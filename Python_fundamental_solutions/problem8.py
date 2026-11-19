
# t = int(input())

# x,y = map(int, input().split())

# for i in range(t):
#     # k,l = map(int, input().split())
#     print(x*y)

## child class or sub class

class Warrior(GameCharacter):
    def __init__(self, name, level, weapon):
        super().__init__(name, level)
        self.weapon = weapon
    
    def display(self):
        return f"{self.name}, is in the level {self.level} with a health of {self.health} and weapon {self.weapon}."
    
    
## Object Creation (Parent object)

g = GameCharater('Alpha', 2)

## child Object

hero = Warrior('Aria', 2, 'Sword')

print(f"the object g is of the type {type(g)} and the object hero is of the type {type(hero)}.")

g.set_health(70)
g.display_info()
g.heal(15)
g.display_info()

hero.display()

# Access the method   from the other class

hero.display_info()
hero.attack()

g.display()

## inheritance - child class use can th attributes (data) and behaviour (methods) of the parent class
## the parent cannot use the attributes and behaviour of the child

class Warrior(GameCharacter):
    def __init__(self, name, level, weapon):
        super().__init__(name, level)
        self.weapon = weapon
        self.name = name 
        self.level = level
    
    def display(self):
        return f"{self.name}, is in the level {self.level} with a health of {self.health} and weapon {self.weapon}."

h = Warrior('Augustus', 2, 'Spear')
h.display_info()

## for a child to inherit the data member from the parent has to be initialized through the child. 
# this is done through super().init(data mambers)

# super() allows common atttributes and attributes exclusive to the parent to be accesed by the child

