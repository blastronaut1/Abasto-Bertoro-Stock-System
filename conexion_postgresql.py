

def start():
    import psycopg2
    import pandas as pd
    import sqlalchemy as al
    from sqlalchemy import create_engine
    from sqlalchemy import text
    pd.set_option('expand_frame_repr', True)
    pd.set_option('display.max_colwidth', 150)
    engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/Stock System Abasto Bertoro")
    sqltext = text
    return pd, engine, al, sqltext






#tabla TIPO
def type_Add():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del TIPO:"))
        Name = str(input("ingrese el Nombre del TIPO:"))
        Descr = str(input("ingrese la descripcion del TIPO:"))
        Img = str(input("ingrese la imagen del TIPO:"))
        Status = str(input("ingrese el status:"))

        query = f"select producto.type_agregar({Id},'{Name}','{Descr}','{Img}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()


def type_Mod():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del TIPO a modificar:"))
        Name = str(input("ingrese el nuevo Nombre del TIPO:"))
        Descr = str(input("ingrese la nueva descripcion del TIPO:"))
        Img = str(input("ingrese la nueva imagen del TIPO:"))
        Status = str(input("ingrese el nuevo status:"))

        query = f"select producto.type_modificar({Id},'{Name}','{Descr}','{Img}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def type_List():
    pd, en, ps, txt = start()
    query=f"select producto.type_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

def type_Delete():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del TIPO a BORRAR:"))

        query = f"select producto.type_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()


#tabla proveedor
def Proveer_Add():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PROVEEDOR:"))
        Name = str(input("ingrese el Nombre del PROVEEDOR:"))
        Descr = str(input("ingrese la descripcion del PROVEEDOR:"))
        Dir = str(input("ingrese la direccion del PROVEEDOR:"))
        Telf = int(input("ingrese el telefono del PROVEEDOR:"))
        Status = str(input("ingrese el status:"))

        query = f"select producto.proveedor_agregar({Id},'{Name}','{Descr}', '{Dir}', '{Telf}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Proveer_Mod():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PROVEEDOR a modificar:"))
        Name = str(input("ingrese el Nuevo* Nombre del PROVEEDOR:"))
        Descr = str(input("ingrese la Nueva* Descripcion del PROVEEDOR:"))
        Dir = str(input("ingrese la Nueva* Direccion del PROVEEDOR:"))
        Telf = int(input("ingrese el Nuevo* Telefono del PROVEEDOR:"))
        Status = str(input("ingrese el Nuevo* status:"))

        query = f"select producto.proveedor_modificar({Id},'{Name}','{Descr}', '{Dir}', '{Telf}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Proveer_List():
    pd, en, ps, txt = start()
    query=f"select producto.proveedor_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

def Proveer_Delete():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PROVEEDOR a BORRAR:"))

        query = f"select producto.proveedor_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()






#tabla precio
def Price_Add():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PRECIO:"))
        fk_itm = int(input("ingrese el tipo (Id del tipo en cuestion) del PRECIO:"))
        fk_pro = int(input("ingrese el proveedor (Id del proveedor en cuestion) que dio el PRECIO:"))
        pri_in = float(input("ingrese el PRECIO de entrada (compra):"))
        pri_out = float(input("ingrese el PRECIO de salida (venta):"))
        Status = str(input("ingrese el status:"))

        query = f"select producto.precios_agregar({Id},{fk_itm},{fk_pro},{pri_in},{pri_out},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Price_Mod():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PRECIO a modificar:"))
        fk_itm = int(input("ingrese el Nuevo* tipo (Id del tipo en cuestion) del PRECIO:"))
        fk_pro = int(input("ingrese el Nuevo* proveedor (Id del proveedor en cuestion) que dio el PRECIO:"))
        pri_in = float(input("ingrese el Nuevo* PRECIO de entrada (compra):"))
        pri_out = float(input("ingrese el Nuevo* PRECIO de salida (venta):"))
        Status = str(input("ingrese el status:"))

        query = f"select producto.precios_modificar({Id},{fk_itm},{fk_pro},{pri_in},{pri_out},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Price_List():
    pd, en, ps, txt = start()
    query=f"select producto.precios_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

def Price_Delete():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del PRECIO a BORRAR:"))

        query = f"select producto.precios_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()







#tabla Item
def Item_Add():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del ITEM:"))
        Name = str(input("ingrese el Nombre del ITEM:"))
        Descr = str(input("ingrese la descripcion del ITEM:"))
        Qnty = int(input("ingrese la cantidad actual del ITEM en stock:"))
        Qnty_min = int(input("ingrese la cantidad minima del ITEM en stock:"))
        fk_type = int(input("ingrese el tipo (Id del tipo en cuestion) del ITEM que es (comida, limpieza, papeleria tec):"))
        fk_pro = int(input("ingrese el proveedor (Id del proveedor en cuestion) que dio el ITEM:"))
        Status = str(input("ingrese el status:"))

        query = f"select producto.item_agregar({Id},'{Name}','{Descr}', {Qnty}, {Qnty_min},{fk_type},{fk_pro},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Item_Mod():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del ITEM a modificar:"))
        Name = str(input("ingrese el Nuevo* Nombre del ITEM:"))
        Descr = str(input("ingrese la Nueva* descripcion del ITEM:"))
        Qnty = int(input("ingrese la Nueva* cantidad actual del ITEM en stock:"))
        Qnty_min = int(input("ingrese la Nueva* cantidad minima del ITEM en stock:"))
        fk_type = int(input("ingrese el Nuevo* tipo (Id del tipo en cuestion) del ITEM que es (comida, limpieza, papeleria tec):"))
        fk_pro = int(input("ingrese el Nuevo* proveedor (Id del proveedor en cuestion) que dio el ITEM:"))
        Status = str(input("ingrese el Nuevo* status:"))

        query = f"select producto.item_modificar({Id},'{Name}','{Descr}', {Qnty}, {Qnty_min},{fk_type},{fk_pro},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Item_List():
    pd, en, ps, txt = start()
    query=f"select producto.item_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

def Item_Delete():
    pd, en, al, txt = start()

    with en.connect() as connection:
        Id = int(input("ingrese el ID del ITEM a BORRAR:"))

        query = f"select producto.item_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()




#type_Search(1)
#Item_List()