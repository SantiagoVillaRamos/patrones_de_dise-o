
def codigo_cliente_vehiculo(fabrica, tipo_vehiculo):
    vehiculo = fabrica.get_vehiculo(tipo_vehiculo)
    print(vehiculo.deliver())