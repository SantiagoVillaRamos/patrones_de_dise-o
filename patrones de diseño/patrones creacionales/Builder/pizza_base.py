

class Pizza:
    
    def __init__(self):
        self.masa = None
        self.salsa = None
        self.topping = None
        
    def __str__(self):
        return f"\n Masa:{self.masa} | salsa: {self.salsa} | Topping: {self.topping} "