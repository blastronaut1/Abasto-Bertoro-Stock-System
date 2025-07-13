import crudGrouper

repeat = True

while (repeat == True):
    print(F'------------MENU----------')
    print(f'con cual tabla quieres trabajar:')
    print(F'1)- Tipo de producto')
    print(F'2)- Proveedor del producto')
    print(F'3)- Precio del producto')
    print(F'4)- el producto (o Item) ensi')
    print(F'--------------------------\n')


    repeat = False
    answer = input(str(f'que deseas hacer?:'))
    match answer:
        case '1': 
            #crudGrouper.start()
            crudGrouper.Type()
        case '2':
            #crudGrouper.start()
            crudGrouper.Proveer()
        case '3':
            #crudGrouper.start()
            crudGrouper.Price()
        case '4':
            #crudGrouper.start()
            crudGrouper.Item()
        case default:
            print(f'Esa opcion no existe compadre!')

    print(F'--------------------------\n')
    cycleagain = input(str(F'Repetir? (Y/N)\n'))
    c = cycleagain.upper()
    if (c == 'Y'):
        repeat = True
    else:
        repeat = False
        #crudGrouper.close()
        break