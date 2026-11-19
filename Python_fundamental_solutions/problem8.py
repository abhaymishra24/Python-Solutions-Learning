
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
