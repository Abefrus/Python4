class Person():
    pass

#* //////////////////////////////////////////////////////////////////////////////////

class Man(Person):
    breakfast = "Donut"

class Woman(Person):
    breakfast = "Croissant"

class Worker(Person):
    breakfast = "Bacon"

class Parent(Person):
    breakfast = "Fruit"

#* //////////////////////////////////////////////////////////////////////////////////

class Wkg_man(Man, Worker):
    pass
 
class Father(Man, Parent):
    pass

class Wkg_women(Woman, Worker):
    pass

class Mother(Woman, Parent):
    pass

class Wkg_mother(Mother, Wkg_women):
    pass

class Wkg_father(Father, Wkg_man):
    pass

#* //////////////////////////////////////////////////////////////////////////////////

Joan = Wkg_mother

Jim = Wkg_man

print(Joan.breakfast)
print(Jim.breakfast)