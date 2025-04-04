"""El handlers se va a encargar de gestionar los diferentes tipos de archivos."""

import json
import csv

class JsonDataHandler:
    """Clase encargada de manejar archivos JSON."""

    def load_data(self, file_path):
        """Carga datos desde un archivo JSON."""
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    
class CsvDataHandler:
    """Clase encargada de manejar archivos CSV."""

    def load_data(self, file_path):
        """Carga datos desde un archivo CSV."""
        with open(file_path, newline='') as file:
            return list(csv.DictReader(file))