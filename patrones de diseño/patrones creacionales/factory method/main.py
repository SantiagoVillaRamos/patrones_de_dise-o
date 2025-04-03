from vehicle_factory.client_code import codigo_cliente_vehiculo
from vehicle_factory.concrete_factory import FabricaCarro, FabricaCamion, FabricaAvion

if __name__=="__main__":
    codigo_cliente_vehiculo(FabricaCarro(), 'sedan')
    codigo_cliente_vehiculo(FabricaCamion(), "remolque")
    codigo_cliente_vehiculo(FabricaAvion(), 'Boing 747')