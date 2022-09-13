from distutils.log import error
import logging
FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename="logs.log", filemode="w",format=FORMAT, datefmt="%H:%M:%S",level=logging.DEBUG)
def menu():
    option = input("*********************************************************************\nMenú principal \n1) Almacenar un texto en la pila. \n2) Visualizar el elemento más largo de la pila. \n3) Visualizar el elemento más corto de la pila. \n4) Imprimir un texto de la pila. \n5) Comparar tamaños de texto. \n6) Sacar un elemento de la pila.\n7) Salir.\nSelecciona una opción:")
    return option
def chequear(max):
    try:
        entrada = input("Indice del elemento a imprimir:")
        logging.info("Indice seleccionado:"+entrada)
        indice = int(entrada)
        if indice not in range(max):
            raise ValueError
    except ValueError as e:
        logging.warning("Se intentó imprimir un texto con un índice no válido.")
        indice=-1
    return indice
        
fin = False
pila = []
while(not(fin)):
    option = int(menu())
    if option < 1 or option > 7:
        logging.warning("Se seleccionó una opción no válida del menú.")
        print("\nPor favor seleccione una opción válida.")
    else:
        logging.info("Opción seleccionada del menú principal: %d.",option)
        if option == 1:
            elemento = input("Ingrese el texto a almacenar en la pila:\n")
            pila.append(elemento)
            print("Se almacenó en la pila el texto: '"+elemento+"' que tiene un largo de "+str(len(elemento))+" caracteres")
            logging.info("Se almacenó en la pila el texto: '%s' que tiene un largo de %d caracteres",elemento,len(elemento))
        elif option == 2:
            largo = len(pila)
            if largo == 0:
                print("La pila se encuentra vacía. Se debe ingresar un elemento antes de solicitar el más largo.")
                logging.warning("Se intentó imprimir el texto más largo en una pila vacía.")
            else:
                indice = 0
                for i in range(len(pila)):
                    if len(pila[i]) >= len(pila[indice]):
                        indice = i
                elemento = pila[indice]
                print(elemento)
                print("Tiene un largo de "+str(len(elemento))+" caracteres")
                logging.info("Elemento más largo está en la posición %d y corresponde a: '%s', que tiene un largo de %d caracteres",indice,elemento,len(elemento))
        elif option == 3:
            largo = len(pila)
            if largo == 0:
                print("La pila se encuentra vacía. Se debe ingresar un elemento antes de solicitar el más corto.")
                logging.warning("Se intentó imprimir el texto más corto en una pila vacía.")
            else:
                indice = 0
                for i in range(len(pila)):
                    if len(pila[i]) <= len(pila[indice]):
                        indice = i
                elemento = pila[indice]
                print(elemento)
                print("Tiene un largo de "+str(len(elemento))+" caracteres")
                logging.info("Elemento más corto está en la posición %d y corresponde a: '%s', que tiene un largo de %d caracteres",indice,elemento, len(elemento))
        elif option == 4:
            largo = len(pila)
            if largo == 0:
                print("La pila se encuentra vacía. Se debe ingresar un elemento antes de solicitar imprimir.")
                logging.warning("Se intentó imprimir un texto en una pila vacía.")
            elif largo ==1:
                print("La pila contiene solo un elemento.")
                elemento = pila[0]
                print(elemento)
                print("Tiene un largo de "+str(len(elemento))+" caracteres")
                logging.info("Elemento de la posición 0 impreso: '%s', tiene un largo de %d caracteres",elemento, len(elemento))
            else:
                print("La pila contiene "+str(largo)+" elementos.")
                print("\nSeleccione una posición entre 0 y "+str(largo-1)+" para ver el elemento de dicha posición.")
                indice = chequear(largo)
                if indice != -1:
                    elemento = pila[indice]
                    print(elemento)
                    print("Tiene un largo de "+str(len(elemento))+" caracteres")
                    logging.info("Elemento de la posición %d impreso: %s",indice,elemento)
                else:
                     print("La posición ingresada no es válida.")
        elif option == 5:
            largo = len(pila)
            if largo < 2:
                print("No hay elementos suficientes para realizar una comparación.")
                logging.warning("No hay elementos suficientes para realizar una comparación.")
            else:
                primer_elemento = ""
                segundo_elemento = ""
                while(primer_elemento == ""):
                    print("\nSeleccione una posición entre 0 y "+str(largo-1)+" para elegir la posición del primer elemento.")
                    indice = int(input("Indice del primer texto:"))
                    if indice >= 0 and indice < largo:
                        primer_elemento = pila[indice]
                        print(primer_elemento)
                        logging.info("Elemento de la posición %d impreso: %s",indice,primer_elemento)
                    else:
                        print("La posición ingresada no es válida.")
                        logging.warning("Se intentó seleccionar un texto con un índice no válido: %d", indice)
                while(segundo_elemento == ""):
                    print("\nSeleccione una posición entre 0 y "+str(largo-1)+" para elegir la posición del segundo elemento.")
                    indice = int(input("Indice del segundo texto:"))
                    if indice >= 0 and indice < largo:
                        segundo_elemento = pila[indice]
                        print(segundo_elemento)
                        logging.info("Elemento de la posición %d impreso: %s",indice,segundo_elemento)
                    else:
                        print("La posición ingresada no es válida.")
                        logging.warning("Se intentó seleccionar un texto con un índice no válido: %d", indice)
                diferencia = len(primer_elemento) - len(segundo_elemento)
                if diferencia > 0:
                    print("El primer texto '"+primer_elemento+"' es más largo que el segundo '"+segundo_elemento+"' por "+str(diferencia)+" caracteres")
                    logging.info("Elemento 1 '%s' es más largo que elemento 2 '%s'.",primer_elemento,segundo_elemento)
                elif diferencia < 0:
                    print("El primer texto '"+primer_elemento+"' es más corto que el segundo '"+segundo_elemento+"', por "+str(-1*diferencia)+" caracteres")
                    logging.info("Elemento 1 '%s' es más corto que elemento 2 '%s'.",primer_elemento,segundo_elemento)
                else:
                    print("Ambos textos '"+ primer_elemento +"' y '"+segundo_elemento+"' son del mismo largo.")
                    logging.info("Elemento 1 '%s' es de igual largo que elemento 2 '%s'.",primer_elemento,segundo_elemento)
        elif option == 6:
            largo = len(pila)
            if largo==0:
                print("La pila se encuentra vacía. Se debe ingresar un elemento antes de solicitar quitar uno.")
                logging.warning("Se intentó sacar un texto de una pila vacía.")
            else:
                elemento = pila.pop()
                print("Se eliminó el elemento '"+elemento+"' de la pila.")
                logging.info("Elemento eliminado de la pila: "+elemento)
        elif option == 7:
            logging.info("Finalizar programa.")
            fin = True