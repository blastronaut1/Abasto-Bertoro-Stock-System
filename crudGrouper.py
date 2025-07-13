import conexion_postgresql

def start():
    conexion_postgresql.start()

def close():
    conexion_postgresql.close()
    
#------------TABLA DE TIPOS
def Type():
    repeat = True

    while (repeat == True):
        print(F'---------- TABLA:TIPO > MENU ----------')
        print(f'defina su consulta')
        print(F'1)- Agregar Data')
        print(F'2)- Modificar Data')
        print(F'3)- Listado de Data')
        print(F'4)- Borrar Data')
        print(F'--------------------------\n')

        repeat = False
        answer = input(str(f'que deseas hacer?:'))
        match answer:
            case '1': 
                conexion_postgresql.type_Add()
            case '2':
                conexion_postgresql.type_Mod()
            case '3':
                conexion_postgresql.type_List()
            case '4':
                conexion_postgresql.type_Delete()
            case default:
                print(f'TABLA:TIPO > Esa opcion no existe compadre!')

        print(F'--------------------------\n')
        cycleagain = input(str(F'TABLA:TIPO > Repetir? (Y/N)\n'))
        c = cycleagain.upper()
        if (c == 'Y'):
            repeat = True
        else:
            repeat = False
            break


#------------TABLA DE PROVEEDORES
def Proveer():
    repeat = True

    while (repeat == True):
        print(F'--------- TABLA:PROVEEDOR > MENU ----------')
        print(f'defina su consulta')
        print(F'1)- Agregar Data')
        print(F'2)- Modificar Data')
        print(F'3)- Listado de Data')
        print(F'4)- Borrar Data')
        print(F'--------------------------\n')


        repeat = False
        answer = input(str(f'que deseas hacer?:'))
        match answer:
            case '1': 
                conexion_postgresql.Proveer_Add()
            case '2':
                conexion_postgresql.Proveer_Mod()
            case '3':
                conexion_postgresql.Proveer_List()
            case '4':
                conexion_postgresql.Proveer_Delete()
            case default:
                print(f'TABLA:PROVEEDOR > Esa opcion no existe compadre!')

        print(F'--------------------------\n')
        cycleagain = input(str(F'TABLA:PROVEEDOR > Repetir? (Y/N)\n'))
        c = cycleagain.upper()
        if (c == 'Y'):
            repeat = True
        else:
            repeat = False
            break


#------------TABLA DE PRECIOS
def Price():
    repeat = True

    while (repeat == True):
        print(F'-------- TABLA:PRECIO > MENU ----------')
        print(f'defina su consulta')
        print(F'1)- Agregar Data')
        print(F'2)- Modificar Data')
        print(F'3)- Listado de Data')
        print(F'4)- Borrar Data')
        print(F'--------------------------\n')


        repeat = False
        answer = input(str(f'que deseas hacer?:'))
        match answer:
            case '1': 
                conexion_postgresql.Price_Add()
            case '2':
                conexion_postgresql.Price_Mod()
            case '3':
                conexion_postgresql.Price_List()
            case '4':
                conexion_postgresql.Price_Delete()
            case default:
                print(f'TABLA:PRECIO > Esa opcion no existe compadre!')

        print(F'--------------------------\n')
        cycleagain = input(str(F'TABLA:PRECIO > Repetir? (Y/N)\n'))
        c = cycleagain.upper()
        if (c == 'Y'):
            repeat = True
        else:
            repeat = False
            break


#------------TABLA DE ITEMS
def Item():
    repeat = True

    while (repeat == True):
        print(F'--------- TABLA:ITEM > MENU ----------')
        print(f'defina su consulta')
        print(F'1)- Agregar Data')
        print(F'2)- Modificar Data')
        print(F'3)- Listado de Data')
        print(F'4)- Borrar Data')
        print(F'--------------------------\n')


        repeat = False
        answer = input(str(f'que deseas hacer?:'))
        match answer:
            case '1': 
                conexion_postgresql.Item_Add()
            case '2':
                conexion_postgresql.Item_Mod()
            case '3':
                conexion_postgresql.Item_List()
            case '4':
                conexion_postgresql.Item_Delete()
            case default:
                print(f'TABLA:ITEM > Esa opcion no existe compadre!')

        print(F'--------------------------\n')
        cycleagain = input(str(F' TABLA:ITEM > Repetir? (Y/N)\n'))
        c = cycleagain.upper()
        if (c == 'Y'):
            repeat = True
        else:
            repeat = False
            break
