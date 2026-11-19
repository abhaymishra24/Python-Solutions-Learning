
# ## child class or sub class

# class Warrior(GameCharacter):
#     def __init__(self, name, level, weapon):
#         super().__init__(name, level)
#         self.weapon = weapon
    
#     def display(self):
#         return f"{self.name}, is in the level {self.level} with a health of {self.health} and weapon {self.weapon}."
    
    
# ## Object Creation (Parent object)

# g = GameCharater('Alpha', 2)

# ## child Object

# hero = Warrior('Aria', 2, 'Sword')

# print(f"the object g is of the type {type(g)} and the object hero is of the type {type(hero)}.")

# g.set_health(70)
# g.display_info()
# g.heal(15)
# g.display_info()

# hero.display()

# # Access the method   from the other class

# hero.display_info()
# hero.attack()

# g.display()

# ## inheritance - child class use can th attributes (data) and behaviour (methods) of the parent class
# ## the parent cannot use the attributes and behaviour of the child

# class Warrior(GameCharacter):
#     def __init__(self, name, level, weapon):
#         super().__init__(name, level)
#         self.weapon = weapon
#         self.name = name 
#         self.level = level
    
#     def display(self):
#         return f"{self.name}, is in the level {self.level} with a health of {self.health} and weapon {self.weapon}."

# h = Warrior('Augustus', 2, 'Spear')
# h.display_info()

# ## for a child to inherit the data member from the parent has to be initialized through the child. 
# # this is done through super().init(data mambers)

# # super() allows common atttributes and attributes exclusive to the parent to be accesed by the child

# hero = Warrior('Aria', 2, 'Sword')
# hero.display_info()

# villian = Warrior('Agustus', 2, 'Spear')
# villian.display_info()

# villian.super().display_info()

# super().display_info()

# Types of Inheritance 

# 1. Single Inheritence

# parent class 

class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Vahical is {self.name}")
        
# Child Class 

class Wheels(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels 
        
    def display(self):
        print(f"Vehicle is a {self.name} having {self.wheels} number of wheels")
        
c = Wheels ('car', 4)
c.display()

# Multilevel Inheritance

class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Vahical is {self.name}")
        
        
class Wheels(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels 
        
    def display(self):
        print(f"Vehicle is a {self.name} having {self.wheels} number of wheels")
        
        
class Status(Wheels):
    def __init__(self, name, wheels, status):
        super().__init__(name, wheels)
        self.status = status
        
    def display(self):
        return f'{self.name} is a vehicle with {self.wheels} wheels and is {self.status}'
    

c = Status('Car', 4, 'Personal')
c1 = Status('Car', 4, 'rented')
c.display()
c1.display()

## In multilevel innheritance - grand parents and parent  common atrribute shuold be 
# initlized in the parent and in the child all the common attributes have to be initialized through
# super()

# Multiple Inheritance (One child having more then one parent (2 or more))

class A:
    def process(self):
        print("Exceuting A")
        
class B(A):
    def process(self):
        print("Exceuting B")
        super().process()
 
class C(B):
    def process(self):
        print("Exceuting C")
        super().process() 
        
class D(B, C):
    def process(self):
        print("Exceuting D")
        super().process()  
        
        
D().process()    

