import tkinter as tk


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.crudTable_state = [0,0]
        self.crudTable_var1 = tk.IntVar()
        self.crudTable_var2 = tk.IntVar()

        #---------GENERAL--------
        self.root.geometry("800x500")
        self.root.title("Base De Datos Abasto Bertoro")
        self.sb_titulo = tk.Label(self.root, text="Stock Sytem", font=('Arial', 22))
        self.sb_titulo.pack(padx=20, pady=5)
        self.sb_subtitulo = tk.Label(self.root, text="sistema de inventario disenado para el Abasto Bertoro", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=20)


        #---------MENU???-------------
        self.crudbtn = tk.Frame(self.root)
        self.crudbtn.columnconfigure(0, weight=1)
        self.crudbtn.columnconfigure(1, weight=1)
        self.crudbtn.columnconfigure(2, weight=1)
        self.crudbtn.columnconfigure(3, weight=1)


        #CRUD 
        self.sb_boton1 = tk.Button(self.crudbtn, text="Agregar", font=('Arial', 15))
        self.sb_boton1.grid(row=0, column=0, sticky=(tk.W+tk.E))

        self.sb_boton2 = tk.Button(self.crudbtn, text="Modificar", font=('Arial', 15))
        self.sb_boton2.grid(row=0, column=1, sticky=(tk.W+tk.E))
    
        self.sb_boton3 = tk.Button(self.crudbtn, text="Listar", font=('Arial', 15))
        self.sb_boton3.grid(row=0, column=2, sticky=(tk.W+tk.E))

        self.sb_boton4 = tk.Button(self.crudbtn, text="Eliminar", font=('Arial', 15))
        self.sb_boton4.grid(row=0, column=3, sticky=(tk.W+tk.E))



    #TABLAS
        self.sb_boton1 = tk.Button(self.crudbtn, text="Tabla TIPO", font=('Arial', 15))
        self.sb_boton1.grid(row=1, column=0, sticky=(tk.W+tk.E))

        self.sb_boton2 = tk.Button(self.crudbtn, text="Tabla PROVEEDOR", font=('Arial', 15))
        self.sb_boton2.grid(row=1, column=1, sticky=(tk.W+tk.E))
    
        self.sb_boton3 = tk.Button(self.crudbtn, text="Tabla PRECIO", font=('Arial', 15))
        self.sb_boton3.grid(row=1, column=2, sticky=(tk.W+tk.E))

        self.sb_boton4 = tk.Button(self.crudbtn, text="Tabla ITEM", font=('Arial', 15))
        self.sb_boton4.grid(row=1, column=3, sticky=(tk.W+tk.E))

        self.crudbtn.pack(fill='x')
        self.sbe_ID = tk.Entry(self.root)
        self.sbe_ID.pack()

        self.root.mainloop()



MyGui()