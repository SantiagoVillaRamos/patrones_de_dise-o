
from pizza_builder import Margarita


maegarita = Margarita()
pizza = (
    maegarita.set_masa("blanda").set_salsa('amarilla').set_topping('salmon').buil()
)
print(pizza)