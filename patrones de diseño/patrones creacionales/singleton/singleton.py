
class Singleton:
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        # si la clase que queremos instanciar no esta en las instancias que hemos creado
        if cls not in cls._instances:
            # usar el objeto como clave; y llamamos al metodo __new__(cls)
            # esto creara una nueva instancia del objeto si no existe.
            cls._instances[cls] = super().__new__(cls)
        # retorna la instancia que queremos abtener
        return cls._instances[cls]
    
objeto1 = Singleton()
objeto2 = Singleton()

print(objeto1 is objeto2)

import sqlite3

class DatabaseConnection(Singleton):
    connection = None
    
    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")
    
    # genera una consulta sql
    def execute_query(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('santiago')")

print(db1 is db2)

db1.close()
db2.close()