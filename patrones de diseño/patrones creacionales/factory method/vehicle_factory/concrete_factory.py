from .creator import FabricaVehiculo
from .product import Carro, Camion, Avion

class FabricaCarro(FabricaVehiculo):
    
    def get_vehiculo(self, tipo_vehiculo):
        return Carro(tipo_vehiculo)
    
class FabricaCamion(FabricaVehiculo):
    
    def get_vehiculo(self, tipo_vehiculo):
        return Camion(tipo_vehiculo)
    
    
class FabricaAvion(FabricaVehiculo):
    
    def get_vehiculo(self, tipo_vehiculo):
        return Avion(tipo_vehiculo)