
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
def type_Add(Id, Name, Descr, Img, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.type_agregar({Id},'{Name}','{Descr}','{Img}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def type_IdName():
    pd, en, ps, txt = start()
    query=f"select type_id,type_name from producto.type"
    df_read_sql = pd.read_sql(query, en)
    return df_read_sql

def type_Mod(Id, Name, Descr, Img, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.type_modificar({Id},'{Name}','{Descr}','{Img}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def type_List():
    pd, en, ps, txt = start()
    query=f"select producto.type_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

    return df_read_sql

def type_Delete(Id):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.type_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()


#tabla proveedor
def Proveer_Add(Id, Name, Descr, Dir, Telf, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.proveedor_agregar({Id},'{Name}','{Descr}', '{Dir}', '{Telf}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Proveer_Mod(Id, Name, Descr, Dir, Telf, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.proveedor_modificar({Id},'{Name}','{Descr}', '{Dir}', '{Telf}','{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Proveer_List():
    pd, en, ps, txt = start()
    query=f"select producto.proveedor_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

    return df_read_sql

def Proveer_Delete(Id):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.proveedor_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()






#tabla precio
def Price_Add(Id, fk_itm, fk_pro, pri_in, pri_out, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.precios_agregar({Id},{fk_itm},{fk_pro},{pri_in},{pri_out},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Price_Mod(Id, fk_itm, fk_pro, pri_in, pri_out, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.precios_modificar({Id},{fk_itm},{fk_pro},{pri_in},{pri_out},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Price_List():
    pd, en, ps, txt = start()
    query=f"select producto.precios_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)
    
    return df_read_sql

def Price_Delete(Id):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.precios_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()







#tabla Item
def Item_Add(Id, Name, Descr, Qnty, Qnty_min, fk_type, fk_pro, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.item_agregar({Id},'{Name}','{Descr}', {Qnty}, {Qnty_min},{fk_type},{fk_pro},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Item_Mod(Id, Name, Descr, Qnty, Qnty_min, fk_type, fk_pro, Status):
    pd, en, al, txt = start()

    with en.connect() as connection:

        query = f"select producto.item_modificar({Id},'{Name}','{Descr}', {Qnty}, {Qnty_min},{fk_type},{fk_pro},'{Status}')"
        result = connection.execute(txt(query))
        connection.commit()

def Item_List():
    pd, en, ps, txt = start()
    query=f"select producto.item_listado()"
    df_read_sql = pd.read_sql(query, en)
    print(df_read_sql)

    return df_read_sql

def Item_Delete(Id):
    pd, en, al, txt = start()

    with en.connect() as connection:
        query = f"select producto.item_eliminar({Id})"
        result = connection.execute(txt(query))
        connection.commit()




