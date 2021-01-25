import numpy as np
import random


#Creo clase Tablero
class Tablero:
    '''
        Documentación de la clase Tablero:
        Tablero con dimensiones 10x10
        flota de 10 barcos
        20 vidas por jugada
        parrilla inicializada con " "
    '''

    dimensiones = (10, 10)  # tupla
    flota = {"B41":4, "B31":3, "B32":3, "B21":2, "B22":2, "B23":2, "B11":1, "B12":1, "B13":1, "B14":1 }                      # diccionario
    vidas = 20
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.parrilla = np.full((10, 10), " ")




    def inicializar_tablero(self) :
        '''
        Documentación de la función inicializar_tablero:
        Se colocan en la parrilla del objeto los barcos definidos en la iniciación de la clase.
        Para cada barco de la flota, se eligen 3 valores aleatorios para colocarlo en la parrilla:
        coordenada x, coordenadad y, y la dirección (horizontal/vertical).
        El barco se despliega en esa coordenada y eje, escogiendo uno de los dos sentidos en ese eje de modo que
        no se salga de la cuadrícula. Igualmente, se comprueba que el espacio que va a ocupar no está ya ocupado
        por otro barco.
        En caso de que se pueda colocar, se buscan nuevas coordenadas y eje.
        :return: la parrilla con los barcos colocados
        '''

        for barco in self.flota.values():        # montamos los barcos de mayor a menor eslora
            barco_no_colocado= True

            while barco_no_colocado:
                origen_x = random.randint(0, 9)
                origen_y = random.randint(0, 9)
                eje = random.randint(0, 1)  # 0 = horizontal, 1 = vertical
                libre = np.full(barco, " ")

                if eje == 0:  # colocar barco en horizontal
                    # si el tamaño no sale del tablero y el hueco está libre, poner barco

                    if (origen_x + barco < 10):  # cabe hacia la derecha   |x-->  |
                        if (self.parrilla[origen_y, origen_x:origen_x + barco:] == libre).all():  # si está libre
                            self.parrilla[origen_y, origen_x:origen_x + barco:] = "O"
                            barco_no_colocado = False
                        else:
                            continue  # no se puede colocar ahí. Nuevo intento

                    else:       # no cabe hacia la derecha, probar hacia la izquierda   |   x|-->
                        if (self.parrilla[origen_y, origen_x:origen_x - barco:-1] == libre).all(): # si está libre
                            self.parrilla[origen_y, origen_x:origen_x - barco:-1] = "O"
                            barco_no_colocado = False
                        else:
                            continue  # no se puede colocar ahí. Nuevo intento

                else:  # colocar barco en vertical (eje=1)
                    if origen_y + barco < 10:  # cabe  hacia abajo  |x-->  |
                        if (self.parrilla[origen_y:origen_y + barco:, origen_x] == libre).all():  # si está libre
                            self.parrilla[origen_y:origen_y + barco:, origen_x] = "O"
                            barco_no_colocado = False
                        else:
                            continue  # no se puede colocar ahí. Nuevo intento

                    else:  # no cabe hacia abajo, probar hacia arriba  |    x|-->
                        if (self.parrilla[origen_y:origen_y - barco:-1, origen_x] == libre).all():  # si está libre
                            self.parrilla[origen_y:origen_y - barco:-1, origen_x] = "O"
                            barco_no_colocado = False
                        else:
                            continue  # no se puede colocar ahí. Nuevo intento

        return self.parrilla

    def mis_disparos(self):     # vista de la parrilla sin barcos
        '''
        Documentación del método mis disparos:

        Foto de la parrilla del objeto en la que se sustituyen los barcos por espacios y se mantienen los impactos
        :return: array numpy con las dimensiones de la parrilla con la foto
        '''
        parrilla_disparos = np.where(self.parrilla == "O", " ",self.parrilla)
        return parrilla_disparos

    def impacto(self, disparo):
        '''
                Documentación del método impacto:

                Tiene como argumento las coordenadas del disparo y marca sobre la parrilla en esa posición,
                X si se disparó a un barco, _ si fue al agua
                :return: variable con el resultado del disparo (tocado/agua)
        '''


        if self.parrilla[disparo[0][0], disparo[0][1]] == "O":
            self.parrilla[disparo[0][0], disparo[0][1]] = "X"
            self.vidas=self.vidas-1                             # si hay impacto pierdes una vida
            impactado="tocado"
        else:
            self.parrilla[disparo[0][0], disparo[0][1]] = "_"
            impactado = "agua"
        return impactado


