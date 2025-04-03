from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def deliver(self):
        pass
    
    
class Carro(Vehiculo):
    
    def __init__(self, model):
        self._model = model
    
    def deliver(self):
        return f"\n Auto {self._model} entregado"
    
    
class Camion(Vehiculo):
    
    def __init__(self, model):
        self._model = model
        
    def deliver(self):
        return f"\n Camion {self._model} entregado"
    

class Avion(Vehiculo):
    
    def __init__(self, model):
        self._model = model
        
    def deliver(self):
        return f"\n El Avion {self._model} entregado"