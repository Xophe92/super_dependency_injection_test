

class DoughFactory():
    def get_dough(self):
        return "pâte avec des pesticides"


class Pizza(DoughFactory):
    def order_pizza(self):
        print(super().get_dough())


Pizza().order_pizza()
help(Pizza)

class DoughFactoryBio(DoughFactory):
    def get_dough(self):
        return "pâte SANS des pesticides !!"

class PizzaBio(Pizza,DoughFactoryBio):
    pass


PizzaBio().order_pizza()
help(PizzaBio)




