from abc import ABC, abstractmethod

class FabricaVehiculo(ABC):
    
    @abstractmethod
    def get_vehiculo(self, tipo_vehiculo):
        pass