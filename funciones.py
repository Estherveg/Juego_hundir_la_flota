import numpy as np

def disparar():
    '''
    Documentacion de la función disparar

    No tiene parámetros de entrada y devuelve un array con las dos coordenadas aleatorias sobre las que se va a disparar
    :return: array numpy
    '''
    disparo = np.random.randint(0,10,(1,2))
    return disparo


def pide_coordenadas (tipo_coordenada):
    '''
    Documentación de la función pide_coordenadas

    Para pedir por pantalla al jugador las coordenadas que quiere introducir y descartar entradas inválidas
    :param tipo_coordenada:
    :return:
    '''
    while True:
        if tipo_coordenada=="horizontal":
            coordenada = input("Coordenada horizontal (0 a 9):")

        else:
            coordenada = input("Coordenada vertical (0 a 9):")

        try:
            coordenada = int(coordenada)

            if 0 <= coordenada <= 9:
                break

            else:
                continue
        except:
            continue

    return coordenada


