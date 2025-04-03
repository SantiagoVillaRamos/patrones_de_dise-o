import copy
from prototype import Prototype

class SystemConfigClone(Prototype):
    
    def __init__(self, configuracion):
        self.configuracion = configuracion
        
    def clonar(self):
        return copy.deepcopy(self)