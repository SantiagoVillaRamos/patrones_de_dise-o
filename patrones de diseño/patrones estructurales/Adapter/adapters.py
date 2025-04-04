"""Se encargan de adaptar las interfaces de los diferentes tipos de archivos a la interfaz que espera el cliente."""

class CsvToJsonAdapter:
    """Adaptador que convierte datos CSV a JSON."""

    def __init__(self, csv_handler):
        self.csv_handler = csv_handler

    def load_data(self, file_path):
        """Carga datos desde un archivo CSV y los convierte a JSON."""
        data = self.csv_handler.load_data(file_path)
        return [dict(row) for row in data]  # Convertir cada fila a un diccionario