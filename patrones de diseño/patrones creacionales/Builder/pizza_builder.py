from pizza_base import Pizza

class PizzaBuilder:
    """Aqui se definen los seters de nuestro objeto"""
    
    def set_masa(self, masa):
        pass
    
    def set_salsa(self, salsa):
        pass
    
    def set_topping(self, topping):
        pass
    
    
"""tipo de pizza"""

class Margarita(PizzaBuilder):
    
    def __init__(self):
        self.pizza = Pizza()
        
    def set_masa(self,masa):
        self.pizza.masa = masa
        return self
        
    def set_salsa(self,salsa):
        self.pizza.salsa = salsa
        return self
        
    def set_topping(self, topping):
        self.pizza.topping = topping
        return self
        
    def buil(self):
        return self.pizza
        
        
        
        