from clases import Tablero
from funciones import disparar ,pide_coordenadas
import numpy as np

'''
El programa tiene un bucle infinito del que se sale cuando uno de los dos jugadores acaba con las vidas del otro.
El jugador tiene un menú principal accesible en cada jugada para elegir qué acción acometer (ver su tablero,
ver los disparos al tablero enemigo , disparar o dejar la partida.

El juego comienza con los dos tableros (jugador y máquina) inicializados con las posiciones de los 10 barcos
colocados aleatoriamente. La inicialización se realiza desde la propia clase del trablero "inicializar_tablero".1

'''

# Declaro constantes


# inicializo variables
turno=0        # 0=mi turno  ;  1=máquina
continuar_partida = True

# CREAR MI TABLERO Y EL DE LA MÁQUINA

mi_tablero = Tablero(0)
mi_tablero.inicializar_tablero()

tablero_maquina = Tablero(1)
tablero_maquina.inicializar_tablero()


# Empieza el juego

print("            *******************************************************")
print("            **               HUNDIR LA FLOTA                     **")
print("            **          Acaba con los barcos enemigos            **")
print("            *******************************************************\n\n")

while continuar_partida:
    if turno == 0: #mi turno
        print("Elige:\n 1. ver tu tablero\n 2. ver tus disparos al enemigo\n 3. disparar\n 4. dejar la partida")
        try:
            opcion = int(input(">>"))
            if opcion == 1:         # ver mi tablero
                print("Mi tablero \n",mi_tablero.parrilla)

            elif opcion ==2:         # ver mis disparos al tablero enemigo2
                print("El tablero enemigo\n",tablero_maquina.mis_disparos())

            elif opcion ==3:        # disparar al tablero enemigo
                impactado = "nuevo turno"  # para que emtre en el bucle y empiece a disparar

                while impactado != "agua":
                    # pido y compruebo coordenadas vertical(y) y horizontal (x)
                    mi_disparo_y = pide_coordenadas("vertical")
                    mi_disparo_x = pide_coordenadas("horizontal")
                    mi_disparo = np.array([[mi_disparo_y, mi_disparo_x]])
                    print("disparo a :", mi_disparo)
                    impactado = tablero_maquina.impacto(mi_disparo)

                    if impactado == "agua":
                        turno = 1

                    print(impactado,"\n")

                    if tablero_maquina.vidas==0:
                        print( "¡¡¡HAS GANADO LA PARTIDA!!!")
                        continuar_partida=False
                        break

            elif opcion == 4:
                print("fin de la partida")
                break

            else:
                print("No tenemos esa opción\n")
                continue
        except:
            print("No es un número del 1 al 4\n")
            continue

    else: # turno de la máquina
        # la máquina dispara a mi tablero
        impactado = "nuevo turno"  #para que emtre en el bucle y empiece a disparar

        while impactado != "agua":
            disparo=disparar()      #mi función disparar
            print("la máquina dispara a :", disparo)
            impactado=mi_tablero.impacto(disparo)

            if impactado == "agua":
                turno=0

            print(impactado,"\n")

            if mi_tablero.vidas == 0:
                print("La máquina te ha ganado :(")
                continuar_partida=False
                break

