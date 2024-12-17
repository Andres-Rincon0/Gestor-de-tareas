from .conexion_db import ConexionDB
from tkinter import messagebox
def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE tareas(
        id_tarea INTEGER,
        nombre VARCHAR(255),
        Descripcion VARCHAR(255),
        Fecha_Entrega VARCHAR(255),
        PRIMARY KEY(id_tarea AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        pass

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE tareas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar registro'
        mensaje = 'Se borró la tabla de la base de datos con exito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar registro'
        mensaje = 'no hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)
    
class Tarea:
    def __init__(self,nombre,Descripcion,Fecha_entrega):
        self.id_tarea = None
        self.nombre = nombre
        self.Descripcion = Descripcion
        self.Fecha_entrega = Fecha_entrega
    
    def __str__(self):
        return f'Tarea[{self.nombre},{self.Descripcion},{self.Fecha_entrega}]'
    
def guardar(tarea):
    conexion = ConexionDB()

    sql=f"""INSERT INTO tareas(nombre, Descripcion,Fecha_entrega)
        VALUES('{tarea.nombre}', '{tarea.Descripcion}','{tarea.Fecha_entrega}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo ='Conexion al registro'
        mensaje = 'No se encontro registro de esta tabla'
        messagebox.showerror(titulo,mensaje)

def Listar():
    conexion = ConexionDB()

    lista_tareas = []
    sql = 'SELECT * FROM tareas'

    try:
        conexion.cursor.execute(sql)
        lista_tareas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje= 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo,mensaje)
    return lista_tareas

def editar(tarea, id_tarea):
    conexion = ConexionDB()

    sql = f"""UPDATE tareas
    SET nombre = '{tarea.nombre}', descripcion='{tarea.Descripcion}',fecha_entrega='{tarea.Fecha_entrega}'
    WHERE id_tarea = {id_tarea}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se a podido editar este registro'
        messagebox.showerror(titulo,mensaje)

def eliminar(id_tarea):
    conexion = ConexionDB()
    sql = f'DELETE FROM tareas WHERE id_tarea = {id_tarea}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'ELiminar de datos'
        mensaje = 'No se a podido Eliminar este registro'
        messagebox.showerror(titulo,mensaje)