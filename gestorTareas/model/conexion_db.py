import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = 'db/tareas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()