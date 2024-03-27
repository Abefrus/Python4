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
 
class Father(Parent, Man):
    pass

class Wkg_women(Worker,Woman):
    pass

class Mother(Parent,Woman):
    pass

class Wkg_mother(Mother, Wkg_women):
    pass

class Wkg_father(Wkg_man, Father):
    pass

#* //////////////////////////////////////////////////////////////////////////////////

Joan = Wkg_mother

Jim = Wkg_man

print(Joan.breakfast)
print(Jim.breakfast)
