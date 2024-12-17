import tkinter as tk
from tkinter import ttk, messagebox
from model.tareas_dao import crear_tabla, borrar_tabla
from model.tareas_dao import Tarea, guardar, Listar, editar,eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB', command= crear_tabla)
    menu_inicio.add_command(label='Eliminar registro en DB',command= borrar_tabla)
    menu_inicio.add_command(label='Salir ', command= root.destroy)
    
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height=320)
        self.root = root
        self.pack()
        self.config(bg='black')
        self.id_nombre = None

        self.campos_gestor_tareas()
        self.deshabilitar_campos()
        self.tabla_tareas()

    def campos_gestor_tareas(self):
        # label de cada campo
        self.label_nombre = tk.Label(self, text= 'Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx=10, pady=10)

        self.label_Descripcion = tk.Label(self, text= 'Descripcion: ')
        self.label_Descripcion.config(font=('Arial', 12, 'bold'))
        self.label_Descripcion.grid(row = 1, column = 0, padx=10, pady=10)

        self.label_Fecha_Entrega = tk.Label(self, text= 'Fecha_Entrega ')
        self.label_Fecha_Entrega.config(font=('Arial', 12, 'bold'))
        self.label_Fecha_Entrega.grid(row = 2, column = 0, padx=10, pady=10)

        # campos de entrada
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width=50,  font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan= 2 )
       
        self.descripcion = tk.StringVar()
        self.entry_Descripcion = tk.Entry(self, textvariable= self.descripcion)
        self.entry_Descripcion.config(width=50,  font=('Arial', 12))
        self.entry_Descripcion.grid(row=1, column=1, padx=10, pady=10, columnspan= 2 )

        self.Fecha_Entrega = tk.StringVar()
        self.entry_Fecha_Entrega = tk.Entry(self, textvariable= self.Fecha_Entrega)
        self.entry_Fecha_Entrega.config(width=50,  font=('Arial', 12))
        self.entry_Fecha_Entrega.grid(row=2, column=1, padx=10, pady=10, columnspan= 2 )

        #Botones 
        self.boton_nuevo = tk.Button(self, text="Nueva tarea", command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg ='white', bg='green', cursor= 'hand2', activebackground='green')
        self.boton_nuevo.grid(row=3, column=0,  padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar tarea", command= self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg ='white', bg='orange', cursor= 'hand2', activebackground='orange')
        self.boton_guardar.grid(row=3, column=1,  padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar tarea", command= self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg ='white', bg='red', cursor= 'hand2', activebackground='red')
        self.boton_cancelar.grid(row=3, column=2,  padx=10, pady=10)

        #metodos 
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.descripcion.set('')
        self.Fecha_Entrega.set('')

        self.entry_Descripcion.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_Fecha_Entrega.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.descripcion.set('')
        self.Fecha_Entrega.set('') 

        self.entry_Descripcion.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_Fecha_Entrega.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):

        tarea = Tarea(
            self.mi_nombre.get(),
            self.descripcion.get(),
            self.Fecha_Entrega.get(),
        )

        if self.id_nombre== None:

            guardar(tarea)
        else:
            editar(tarea, self.id_nombre)
            self.tabla_tareas()

        self.deshabilitar_campos()

    

    def tabla_tareas(self):

        #Recuperar lista de tareas
        self.lista_tareas = Listar()
        self.lista_tareas.reverse()

        self.tabla = ttk.Treeview(self,column=('Nombre', 'Descripcion', 'Fecha_Entrega'))
        self.tabla.grid(row=4, column=0, columnspan=4,sticky='nse')

        #Scrollbar para  la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self, orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row= 4, column= 4, sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DESCRIPCION')
        self.tabla.heading('#3', text='Fecha_Entrega')

        #Iterar la lista de Tareas
        for p in self.lista_tareas:
            self.tabla.insert('',0, text=p[0], 
        values=(p[1], p[2], p[3]))

        # Botones Editar
        self.boton_Editar = tk.Button(self, text="Editar tarea",command= self.editar_datos)
        self.boton_Editar.config(width=20, font=('Arial', 12, 'bold'), fg ='blue', bg='#08a0bf', cursor= 'hand2', activebackground='blue')
        self.boton_Editar.grid(row=5, column=0,  padx=10, pady=10)


        # botones de eliminar
        self.boton_Eliminar = tk.Button(self, text="Eliminar tarea", command=self.eliminar_datos)
        self.boton_Eliminar.config(width=20, font=('Arial', 12, 'bold'), fg ='white', bg='red', cursor= 'hand2', activebackground='red')
        self.boton_Eliminar.grid(row=5, column=1,  padx=10, pady=10)

    def editar_datos(self):

    
        try:
            self.id_tarea = self.tabla.item(self.tabla.selection())['text']
            self.nombre_tarea = self.tabla.item(self.tabla.selection())['values'][0]
            self.Descripcion_tarea = self.tabla.item(self.tabla.selection())['values'][1]
            self.Fecha_tarea = self.tabla.item(self.tabla.selection())['values'][0]

            self.habilitar_campos()
            self.entry_nombre.insert(0,self.nombre_tarea)
            self.entry_Descripcion.insert(0,self.Descripcion_tarea)
            self.entry_Fecha_Entrega.insert(0,self.Fecha_tarea)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'Debe seleccionar un registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_tarea = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_tarea)
            self.tabla_tareas()
        except:
            titulo = 'ELiminar de datos'
            mensaje = 'No se a podido Eliminar este registro'
            messagebox.showerror(titulo,mensaje)