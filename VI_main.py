import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import VI_conexion_postgresql as STOCKSYSTEM
class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.commit = False
        print(self.commit)
        #---------GENERAL--------
        self.root.geometry("800x500")
        self.root.title("Base De Datos Abasto Bertoro")
        self.sb_titulo = tk.Label(self.root, text="Stock Sytem", font=('Arial', 22))
        self.sb_titulo.pack(padx=20, pady=20)
        self.sb_subtitulo = tk.Label(self.root, text="sistema de inventario disenado para el Abasto Bertoro", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=20)

        self.menubar = tk.Menu(self.root)

        self.addmenu = tk.Menu(self.menubar, tearoff=0)
        self.addmenu.add_command(label="AÑADIR tipo de producto", command=self.addType)
        self.addmenu.add_separator()
        self.addmenu.add_command(label="AÑADIR proveedor", command=self.addProveer)
        self.addmenu.add_separator()
        self.addmenu.add_command(label="AÑADIR precio del producto", command=self.addPrize)
        self.addmenu.add_separator()
        self.addmenu.add_command(label="AÑADIR producto/item", command=self.addItem)
        self.addmenu.add_separator()

        
        self.changemenu = tk.Menu(self.menubar, tearoff=0)
        self.changemenu.add_command(label="MODIFICAR tipo de producto", command=self.modType)
        self.changemenu.add_separator()
        self.changemenu.add_command(label="MODIFICAR proveedor", command=self.modProveer)
        self.changemenu.add_separator()
        self.changemenu.add_command(label="MODIFICAR precio del producto", command=self.modPrize)
        self.changemenu.add_separator()
        self.changemenu.add_command(label="MODIFICAR producto/item", command=self.modItem)
        self.changemenu.add_separator()

        self.listmenu = tk.Menu(self.menubar, tearoff=0)
        self.listmenu.add_command(label="LISTAR tipos de productos", command=self.listType)
        self.listmenu.add_separator()
        self.listmenu.add_command(label="LISTAR proveedores", command=self.listProveer)
        self.listmenu.add_separator()
        self.listmenu.add_command(label="LISTAR precios de los productos", command=self.listPrize)
        self.listmenu.add_separator()
        self.listmenu.add_command(label="LISTAR productos/items", command=self.listItem)
        self.listmenu.add_separator()

        self.deletemenu = tk.Menu(self.menubar, tearoff=0)
        self.deletemenu.add_command(label="BORRAR tipo de producto", command=self.delType)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR proveedore", command=self.delProveer)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR precio del producto", command=self.delPrize)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR producto/item", command=self.delItem)
        self.deletemenu.add_separator()

        self.menubar.add_cascade(menu=self.addmenu,label="añadir Datos")
        self.menubar.add_cascade(menu=self.changemenu,label="Modificar Datos")
        self.menubar.add_cascade(menu=self.listmenu,label="Listar Datos")
        self.menubar.add_cascade(menu=self.deletemenu,label="Borrar Datos")
        self.root.config(menu=self.menubar)


        self.root.mainloop()

    #---------TIPO-------
    def addType(self):

        #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Añadir Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Añadir Datos:\n Tipo de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes Añadir las clasificaciones\n que quieras darles a tus productos!\n(ejemplo: comida, limpieza, papeleria, etc)", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Img = tk.StringVar()
        self.Status = tk.StringVar()

        #data
        self.idLabel = tk.Label(self.crudWindow, text="ID del tipo")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nombre del tipo")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Descripcion del tipo")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack(padx=7, pady=7)

        self.imgLabel = tk.Label(self.crudWindow, text="Imagen del tipo")
        self.imgLabel.pack()
        self.imgEntry = tk.Entry(self.crudWindow, textvariable=self.Img)
        self.imgEntry.pack(padx=7, pady=7)


        label1 = tk.Label(self.crudWindow, text="Es esta categoria/tipo en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitType(int(self.Id.get()),self.Name.get(),self.descr.get(),self.Img.get(),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)

    def modType():
        pass
    def listType():
        pass
    def delType():
        pass
    #--------PROVEEDOR--------
    def addProveer():
        pass
    def modProveer():
        pass
    def listProveer():
        pass
    def delProveer():
        pass
    #---------PRECIO---------
    def addPrize():
        pass
    def modPrize():
        pass
    def listPrize():
        pass
    def delPrize():
        pass
    #---------ITEM------
    def addItem():
        pass
    def modItem():
        pass
    def listItem():
        pass
    def delItem():
        pass
    
    
    def commitType(self,r1,r2,r3,r4,r5):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.type_Add(r1, r2, r3, r4, r5)
            print("ocurrio")



MyGui()