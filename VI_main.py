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

        self.searchmenu = tk.Menu(self.menubar, tearoff=0)
        self.searchmenu.add_command(label="BUSCAR UN tipo de producto", command=self.searchType)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="BUSCAR UN proveedor", command=self.searchProveer)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="BUSCAR UN precio de producto", command=self.searchPrize)
        self.searchmenu.add_separator()
        self.searchmenu.add_command(label="BUSCAR UN producto/item", command=self.searchItem)
        self.searchmenu.add_separator()

        self.deletemenu = tk.Menu(self.menubar, tearoff=0)
        self.deletemenu.add_command(label="BORRAR tipo de producto", command=self.delType)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR proveedor", command=self.delProveer)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR precio del producto", command=self.delPrize)
        self.deletemenu.add_separator()
        self.deletemenu.add_command(label="BORRAR producto/item", command=self.delItem)
        self.deletemenu.add_separator()

        self.menubar.add_cascade(menu=self.addmenu,label="añadir Datos")
        self.menubar.add_cascade(menu=self.changemenu,label="Modificar Datos")
        self.menubar.add_cascade(menu=self.listmenu,label="Listar Datos")
        self.menubar.add_cascade(menu=self.searchmenu,label="Buscar Datos")
        self.menubar.add_cascade(menu=self.deletemenu,label="Borrar Datos")
        self.root.config(menu=self.menubar)


        self.root.mainloop()





    #---------TIPO-------
    #anadir tipo
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
        #self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        #self.Img = tk.StringVar()
        self.Status = tk.StringVar()

        #data
        #self.idLabel = tk.Label(self.crudWindow, text="ID del tipo")
        #self.idLabel.pack()
        #self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        #self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nombre del tipo")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Descripcion del tipo")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack(padx=7, pady=7)

        #self.imgLabel = tk.Label(self.crudWindow, text="Imagen del tipo")
        #self.imgLabel.pack()
        #self.imgEntry = tk.Entry(self.crudWindow, textvariable=self.Img)
        #self.imgEntry.pack(padx=7, pady=7)


        label1 = tk.Label(self.crudWindow, text="Es esta categoria/tipo en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitType(self.Name.get(),self.descr.get(),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)

    #modificar tipo
    def modType(self):
        #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Modificar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Modificar Datos:\n Tipo de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes modificar ciertos datos de\n la categoria de producto\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        #self.idOptions = STOCKSYSTEM.type_IdName()
        self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Img = tk.StringVar()
        self.Status = tk.StringVar()

        #data
        self.idLabel = tk.Label(self.crudWindow, text="ID del tipo a cambiar\n(solo funcionara con tipos ya existentes)")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="nuevo Nombre del tipo")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="nueva Descripcion del tipo a cambiar")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack(padx=7, pady=7)

        #self.imgLabel = tk.Label(self.crudWindow, text="nueva Imagen del tipo a cambiar")
        #self.imgLabel.pack()
        #self.imgEntry = tk.Entry(self.crudWindow, textvariable=self.Img)
        #self.imgEntry.pack(padx=7, pady=7)

        label1 = tk.Label(self.crudWindow, text="Es esta categoria/tipo en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitType2(int(self.Id.get()),self.Name.get(),self.descr.get(),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)      

    #listar tipo
    def listType(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("Lista de Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Lista de Datos:\n Tipo de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca se listan todas las categorias\n(ejemplo: comida, limpieza, papeleria, etc)\n presentes en sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)
        
        self.list = STOCKSYSTEM.type_List()
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    #buscar tipo
    def searchType(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Buscar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Buscar Datos:\n Tipo de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes buscar\n una categoria de producto en especifico\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del tipo a buscar")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="buscar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.searchType2(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 

    def searchType2(self,r1):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("resultados de busqueda")
        
        self.list = STOCKSYSTEM.type_Search(r1)
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    #borrartipo
    def delType(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Eliminar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Eliminar Datos:\n Tipo de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes eliminar\n la categoria de producto\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del tipo a eliminar\n(ESTA ACCION ES PERMANENTE)")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="eliminar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.commitType3(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20)  



    #--------PROVEEDOR--------
    def addProveer(self):
         #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Añadir Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Añadir Datos:\n Proveedores de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes añadir un proveedor\n de uno de los productos que guardas en el sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        #self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Dir = tk.StringVar()
        self.Telf = tk.StringVar()
        self.Status = tk.StringVar()

        #data
        #self.idLabel = tk.Label(self.crudWindow, text="ID del Proveedor")
        #self.idLabel.pack()
        #self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        #self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nombre del Proveedor")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Descripcion del Proveedor")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack(padx=7, pady=7)

        self.dirLabel = tk.Label(self.crudWindow, text="Direccion del proveedor")
        self.dirLabel.pack()
        self.dirEntry = tk.Entry(self.crudWindow, textvariable=self.Dir)
        self.dirEntry.pack(padx=7, pady=7)

        self.telLabel = tk.Label(self.crudWindow, text="Telefono del Proveedor")
        self.telLabel.pack()
        self.telEntry = tk.Entry(self.crudWindow, textvariable=self.Telf)
        self.telEntry.pack(padx=7, pady=7)


        label1 = tk.Label(self.crudWindow, text="Es este Proveedor en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitProveer(self.Name.get(),self.descr.get(),self.Dir.get(),self.Telf.get(),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)

    def modProveer(self):
         #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Modificar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Modificar Datos:\n Proveedores de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes Modificar los datos un proveedor\n de uno de los productos que guardas en el sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Dir = tk.StringVar()
        self.Telf = tk.StringVar()
        self.Status = tk.StringVar()

        #data
        self.idLabel = tk.Label(self.crudWindow, text="ID del Proveedor a proveedor")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nuevo Nombre del Proveedor")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Nueva Descripcion del Proveedor")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack(padx=7, pady=7)

        self.dirLabel = tk.Label(self.crudWindow, text="Nueva Direccion del proveedor")
        self.dirLabel.pack()
        self.dirEntry = tk.Entry(self.crudWindow, textvariable=self.Dir)
        self.dirEntry.pack(padx=7, pady=7)

        self.telLabel = tk.Label(self.crudWindow, text="Nueva Telefono del Proveedor")
        self.telLabel.pack()
        self.telEntry = tk.Entry(self.crudWindow, textvariable=self.Telf)
        self.telEntry.pack(padx=7, pady=7)


        label1 = tk.Label(self.crudWindow, text="Es este Proveedor en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitProveer2(int(self.Id.get()),self.Name.get(),self.descr.get(),self.Dir.get(),self.Telf.get(),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)

    def listProveer(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("800x600")
        self.crudWindow.title("Lista de Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Lista de Datos:\n Proveedor de los producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca se listan todos los Proveedores\n presentes en sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)
        
        self.list = STOCKSYSTEM.Proveer_List()
        self.Output = tk.Text(self.crudWindow, height = 75, width = 75, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    #buscar tipo
    def searchProveer(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Buscar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Buscar Datos:\n proveedor", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes buscar\n un proveedor en especifico\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del proveedor a buscar")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="buscar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.searchProveer2(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 

    def searchProveer2(self,r1):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("resultados de busqueda")
        
        self.list = STOCKSYSTEM.Proveer_Search(r1)
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    def delProveer(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Eliminar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Eliminar Datos:\n Proveedor de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes eliminar\n el proveedor que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del Proveedor a eliminar\n(ESTA ACCION ES PERMANENTE)")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="eliminar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.commitProveer3(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20)  







    #---------PRECIO---------
    def addPrize(self):
         #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Añadir Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Añadir Datos:\n Precio de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes añadir un registro sobre los movimientos capitales\n acerca de un producto", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        #self.Id = tk.IntVar()
        self.fk_itm = tk.IntVar()
        self.fk_pro = tk.IntVar()
        self.pri_in = tk.DoubleVar()
        self.pri_out = tk.DoubleVar()
        self.Status = tk.StringVar()

        #data
        #self.idLabel = tk.Label(self.crudWindow, text="ID del registro del precio")
        #self.idLabel.pack()
        #self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        #self.idEntry.pack(padx=7, pady=7)

        self.fkitmLabel = tk.Label(self.crudWindow, text="a cual item le pertenece este registro?\n ingrese el Id")
        self.fkitmLabel.pack()
        self.fkitmEntry = tk.Entry(self.crudWindow, textvariable=self.fk_itm)
        self.fkitmEntry.pack(padx=7, pady=7)

        self.fkproLabel = tk.Label(self.crudWindow, text="a cual proveedor le pertenece este registro?\n ingrese el Id")
        self.fkproLabel.pack()
        self.fkproEntry = tk.Entry(self.crudWindow, textvariable=self.fk_pro)
        self.fkproEntry.pack(padx=7, pady=7)

        self.priinLabel = tk.Label(self.crudWindow, text="Ingrese el precio de compra del producto\n (cuanto te costo conseguirlo)")
        self.priinLabel.pack()
        self.priinEntry = tk.Entry(self.crudWindow, textvariable= self.pri_in)
        self.priinEntry.pack(padx=7, pady=7)

        self.prioutLabel = tk.Label(self.crudWindow, text="Ingrese el precio de venta del producto\n (a cuanto lo vas a vender?)")
        self.prioutLabel.pack()
        self.prioutEntry = tk.Entry(self.crudWindow, textvariable= self.pri_out)
        self.prioutEntry.pack(padx=7, pady=7)

        label1 = tk.Label(self.crudWindow, text="Es este Registro de precio en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitPrize(int(self.fk_itm.get()),int(self.fk_pro.get()),float(self.pri_in.get()),float(self.pri_out.get()),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)


    def modPrize(self):
        #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Modificar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Modificar Datos:\n Precio de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes modificar un registro sobre los movimientos capitales\n acerca de un producto", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        self.Id = tk.IntVar()
        self.fk_itm = tk.IntVar()
        self.fk_pro = tk.IntVar()
        self.pri_in = tk.DoubleVar()
        self.pri_out = tk.DoubleVar()
        self.Status = tk.StringVar()

        #data
        self.idLabel = tk.Label(self.crudWindow, text="ID del registro del precio a modificar")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.fkitmLabel = tk.Label(self.crudWindow, text="a cual item le pertenece este registro?\n ingrese el Id a cambiar")
        self.fkitmLabel.pack()
        self.fkitmEntry = tk.Entry(self.crudWindow, textvariable=self.fk_itm)
        self.fkitmEntry.pack(padx=7, pady=7)

        self.fkproLabel = tk.Label(self.crudWindow, text="a cual proveedor le pertenece este registro?\n ingrese el Id a cambiar")
        self.fkproLabel.pack()
        self.fkproEntry = tk.Entry(self.crudWindow, textvariable=self.fk_pro)
        self.fkproEntry.pack(padx=7, pady=7)

        self.priinLabel = tk.Label(self.crudWindow, text="Ingrese el nuevo precio de compra del producto\n (cuanto te costo conseguirlo)")
        self.priinLabel.pack()
        self.priinEntry = tk.Entry(self.crudWindow, textvariable= self.pri_in)
        self.priinEntry.pack(padx=7, pady=7)

        label1 = tk.Label(self.crudWindow, text="Es este Registro de precio en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitPrize2(int(self.Id.get()),int(self.fk_itm.get()),int(self.fk_pro.get()),float(self.pri_in.get()),float(self.pri_out.get()),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)


    def listPrize(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("800x600")
        self.crudWindow.title("Lista de Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Lista de Datos:\n Precio de los producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca se listan todos los registros capitales\n presentes en sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)
        
        self.list = STOCKSYSTEM.Price_List()
        self.Output = tk.Text(self.crudWindow, height = 75, width = 75, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    #buscar tipo
    def searchPrize(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Buscar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Buscar Datos:\n precio", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes buscar\n una registro capital en especifico\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del registro capital")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="buscar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.searchPrize2(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 

    def searchPrize2(self,r1):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("resultados de busqueda")
        
        self.list = STOCKSYSTEM.Price_Search(r1)
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)


    def delPrize(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Eliminar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Eliminar Datos:\n Precio de producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes eliminar\n el registro capital que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del registro capital a eliminar\n(ESTA ACCION ES PERMANENTE)")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="eliminar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.commitPrize3(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 



    #---------ITEM------
    def addItem(self):
        #titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x800")
        self.crudWindow.title("Añadir Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Añadir Datos:\n Productos/Items", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes añadir un Producto/Item al Stock", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        #self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Qnty = tk.IntVar()
        self.Qnty_min = tk.IntVar()
        self.fk_type = tk.IntVar()
        self.fk_pro = tk.IntVar()
        self.Status = tk.StringVar()

        #data
        #self.idLabel = tk.Label(self.crudWindow, text="ID del Producto")
        #self.idLabel.pack()
        #self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        #self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nombre del Producto")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Descripcion del Producto")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack()

        self.qntyLabel = tk.Label(self.crudWindow, text="cuanta cantidad de este\n producto se tiene actualmente?")
        self.qntyLabel.pack()
        self.qntyEntry = tk.Entry(self.crudWindow, textvariable=self.Qnty)
        self.qntyEntry.pack(padx=7, pady=7)

        self.qnty1Label = tk.Label(self.crudWindow, text="cual es la cantidad MINIMA de este\n producto se tiene actualmente?")
        self.qnty1Label.pack()
        self.qnty1Entry = tk.Entry(self.crudWindow, textvariable=self.Qnty_min)
        self.qnty1Entry.pack(padx=7, pady=7)

        self.fktypeLabel = tk.Label(self.crudWindow, text="que clase de producto es este?\n (Ingrese el Id de la categoria)")
        self.fktypeLabel.pack()
        self.fktypeEntry = tk.Entry(self.crudWindow, textvariable= self.fk_type)
        self.fktypeEntry.pack(padx=7, pady=7)
        
        self.fkproLabel = tk.Label(self.crudWindow, text="quien proporciono este producto?\n (Ingrese el Id del proveedor)")
        self.fkproLabel.pack()
        self.fkproEntry = tk.Entry(self.crudWindow, textvariable= self.fk_pro)
        self.fkproEntry.pack(padx=7, pady=7)

        label1 = tk.Label(self.crudWindow, text="Esta este producto en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitItem(self.Name.get(),self.descr.get(),int(self.Qnty.get()),int(self.Qnty_min.get()),int(self.fk_type.get()),int(self.fk_pro.get()),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)



    def modItem(self):
        # titulo
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x800")
        self.crudWindow.title("Modificar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Modificar Datos:\n Productos/Items", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes Modificar la data\n de un Producto/Item en el Stock", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)


        #variables
        self.Id = tk.IntVar()
        self.Name = tk.StringVar()
        self.descr = tk.StringVar()
        self.Qnty = tk.IntVar()
        self.Qnty_min = tk.IntVar()
        self.fk_type = tk.IntVar()
        self.fk_pro = tk.IntVar()
        self.Status = tk.StringVar()

        #data
        self.idLabel = tk.Label(self.crudWindow, text="ID del Producto a modificar")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable= self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.nameLabel = tk.Label(self.crudWindow, text="Nuevo Nombre del Producto")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.crudWindow, textvariable=self.Name)
        self.nameEntry.pack(padx=7, pady=7)

        self.descrLabel = tk.Label(self.crudWindow, text="Nueva Descripcion del Producto")
        self.descrLabel.pack()
        self.descrEntry = tk.Entry(self.crudWindow, textvariable=self.descr)
        self.descrEntry.pack()

        self.qntyLabel = tk.Label(self.crudWindow, text="cuanta cantidad de este\n producto se tiene actualmente?")
        self.qntyLabel.pack()
        self.qntyEntry = tk.Entry(self.crudWindow, textvariable=self.Qnty)
        self.qntyEntry.pack(padx=7, pady=7)

        self.qnty1Label = tk.Label(self.crudWindow, text="cual es la cantidad MINIMA de este\n producto se tiene actualmente?")
        self.qnty1Label.pack()
        self.qnty1Entry = tk.Entry(self.crudWindow, textvariable=self.Qnty_min)
        self.qnty1Entry.pack(padx=7, pady=7)

        self.fktypeLabel = tk.Label(self.crudWindow, text="que clase de producto es este?\n (Ingrese el Nuevo Id de la categoria)")
        self.fktypeLabel.pack()
        self.fktypeEntry = tk.Entry(self.crudWindow, textvariable= self.fk_type)
        self.fktypeEntry.pack(padx=7, pady=7)
        
        self.fkproLabel = tk.Label(self.crudWindow, text="quien proporciono este producto?\n (Ingrese el Nuevo Id del proveedor)")
        self.fkproLabel.pack()
        self.fkproEntry = tk.Entry(self.crudWindow, textvariable= self.fk_pro)
        self.fkproEntry.pack(padx=7, pady=7)

        label1 = tk.Label(self.crudWindow, text="Esta este producto en uso?")
        label1.pack()
        self.statusLabel = tk.Checkbutton(self.crudWindow, text="chequea esto si ese es el caso", variable=self.Status, onvalue="A", offvalue="I")
        self.statusLabel.pack()

        self.confirm = tk.Button(self.crudWindow,text="enviar informacion a la base de datos", font=('Arial', 15),command=lambda:self.commitItem2(int(self.Id.get()),self.Name.get(),self.descr.get(),int(self.Qnty.get()),int(self.Qnty_min.get()),int(self.fk_type.get()),int(self.fk_pro.get()),self.Status.get()))
        self.confirm.pack(padx=7, pady=20)

    def listItem(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("Lista de Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Lista de Datos:\n producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca se listan todos los Productos\n presentes en sistema", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)
        
        self.list = STOCKSYSTEM.Item_List()
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)
 
    #buscar tipo
    def searchItem(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Buscar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Buscar Datos:\n Producto", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes buscar\n un producto en especifico\n(ejemplo: comida, limpieza, papeleria, etc)\n que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del producto a buscar")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="buscar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.searchItem2(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 

    def searchItem2(self,r1):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("1000x600")
        self.crudWindow.title("resultados de busqueda")
        
        self.list = STOCKSYSTEM.Item_Search(r1)
        self.Output = tk.Text(self.crudWindow, height = 75, width = 120, bg = "light cyan")
        self.Output.pack()
        self.Output.insert(tk.END, self.list)

    def delItem(self):
        self.crudWindow = tk.Toplevel()
        self.crudWindow.resizable(width=False,height=False)
        self.crudWindow.geometry("400x600")
        self.crudWindow.title("Eliminar Datos")
        self.sb_titulo = tk.Label(self.crudWindow, text="Eliminar Datos:\n ProductoS", font=('Arial', 15))
        self.sb_titulo.pack(padx=20, pady=10)
        self.sb_subtitulo = tk.Label(self.crudWindow, text="aca puedes eliminar\n el Producto que desees!", font=('Arial', 11))
        self.sb_subtitulo.pack(padx=20, pady=10)

        self.Id = tk.IntVar()

        self.idLabel = tk.Label(self.crudWindow, text="ID del Producto/Item a eliminar\n(ESTA ACCION ES PERMANENTE)")
        self.idLabel.pack()
        self.idEntry = tk.Entry(self.crudWindow, textvariable=self.Id)
        self.idEntry.pack(padx=7, pady=7)

        self.confirm = tk.Button(self.crudWindow,text="eliminar Informacion en la base de datos", font=('Arial', 15),command=lambda:self.commitItem3(int(self.Id.get())))
        self.confirm.pack(padx=7, pady=20) 

    
    









    #--------COMITEO COMITEO TETETEO
    def commitType(self,r1,r2,r3):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.type_Add(r1, r2, r3)
            print("ocurrio")

    def commitType2(self,r1,r2,r3,r4):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.type_Mod(r1, r2, r3, r4)
            print("ocurrio")

    def commitType3(self,r1):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?\n Esta accion es permanente y muy delicada, proceder con cautela')
        if (answer==True):
            STOCKSYSTEM.type_Delete(r1)
            print("ocurrio")

    def commitProveer(self,r1,r2,r3,r4,r5):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Proveer_Add(r1, r2, r3, r4, r5)
            print("ocurrio")

    def commitProveer2(self,r1,r2,r3,r4,r5,r6):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Proveer_Mod(r1, r2, r3, r4, r5, r6)
            print("ocurrio")

    def commitProveer3(self,r1):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?\n Esta accion es permanente y muy delicada, proceder con cautela')
        if (answer==True):
            STOCKSYSTEM.Proveer_Delete(r1)
            print("ocurrio")


    def commitPrize(self,r1,r2,r3,r4,r5):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Price_Add(r1, r2, r3, r4, r5)
            print("ocurrio")

    def commitPrize2(self,r1,r2,r3,r4,r5,r6):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Price_Mod(r1, r2, r3, r4, r5, r6)
            print("ocurrio")

    def commitPrize3(self,r1):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?\n Esta accion es permanente y muy delicada, proceder con cautela')
        if (answer==True):
            STOCKSYSTEM.Price_Delete(r1)
            print("ocurrio")


    def commitItem(self,r1,r2,r3,r4,r5,r6,r7):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Item_Add(r1, r2, r3, r4, r5, r6, r7)
            print("ocurrio")

    def commitItem2(self,r1,r2,r3,r4,r5,r6,r7,r8):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?')
        if (answer==True):
            STOCKSYSTEM.Item_Mod(r1, r2, r3, r4, r5, r6,r7,r8)
            print("ocurrio")

    def commitItem3(self,r1):
        answer = messagebox.askyesno('confirmacion','estas seguro de hacer estos cambios a la base de datos?\n Esta accion es permanente y muy delicada, proceder con cautela')
        if (answer==True):
            STOCKSYSTEM.Item_Delete(r1)
            print("ocurrio")
MyGui()