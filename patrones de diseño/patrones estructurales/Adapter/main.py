
from adapters import CsvToJsonAdapter
from data_handlers import CsvDataHandler, JsonDataHandler

def load_and_display_data(file_path, file_type):
    
    data = file_path.load_data(file_type)
    print(data)
    
if __name__ == "__main__":
    # Crear instancias de los manejadores de datos
    json_handler = JsonDataHandler()
    json_file_path = 'data/sample_data.json'
    load_and_display_data(json_handler, json_file_path)
    
    csv_handler = CsvDataHandler()
    csv_file_path = 'data/sample_data.csv'
    csv_adapter = CsvToJsonAdapter(csv_handler)
    load_and_display_data(csv_adapter, csv_file_path)
