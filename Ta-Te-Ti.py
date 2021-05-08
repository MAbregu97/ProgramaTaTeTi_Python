def imprimir_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print('|'+fila[i], end='|\n')
            else:
                print('|'+fila[i], end='')

def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo ='X'
    else:
        simbolo = 'O'
    if posicion == 1:
        if tablero [2][0] == ' ':
            tablero[2][0] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 2:
        if tablero [2][1] == ' ':
            tablero[2][1] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 3:
        if tablero [2][2] == ' ':
            tablero[2][2] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 4:
        if tablero [1][0] == ' ':
            tablero[1][0] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 5:
        if tablero [1][1] == ' ':
            tablero[1][1] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 6:
        if tablero [1][2] == ' ':
            tablero[1][2] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 7:
        if tablero [0][0] == ' ':
            tablero[0][0] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 8:
        if tablero [0][1] == ' ':
            tablero[0][1] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion == 9:
        if tablero [0][2] == ' ':
            tablero[0][2] = simbolo
            return 0
        else:
            return 'Esa posición ya esta ocupada.'
    if posicion !=1 and posicion !=2 and posicion !=3 and posicion !=4 and posicion !=5 and posicion !=6 and posicion !=7 and posicion !=8 and posicion !=9:
        return '\n¡Ese número no es válido! Por favor, elija unicamente un número del 1 al 9.\n'
        

def hay_ganador (tablero):
    for simbolo in ['X','O']:
        fila_0 = tablero[0][0] == simbolo and tablero[0][1] == simbolo and tablero[0][2] == simbolo
        fila_1 = tablero[1][0] == simbolo and tablero[1][1] == simbolo and tablero[1][2] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][1] == simbolo and tablero[2][2] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[1][0] == simbolo and tablero[2][0] == simbolo
        columna_1 = tablero[0][1] == simbolo and tablero[1][1] == simbolo and tablero[2][1] == simbolo        
        columna_2 = tablero[0][2] == simbolo and tablero[1][2] == simbolo and tablero[2][2] == simbolo
        diagonal_1 = tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo        
        diagonal_2 = tablero[2][0] == simbolo and tablero[1][1] == simbolo and tablero[0][2] == simbolo

        if fila_0 or fila_1 or fila_2 or columna_0 or columna_1 or columna_2 or diagonal_1 or diagonal_2:
            if simbolo == 'X':
                return 1
            elif simbolo == 'O':
                return 2
            break

tablero = [
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' '],
]

ejemplo = [
    ['7' , '8' , '9'],
    ['4' , '5' , '6'],
    ['1' , '2' , '3'],
]

turno_1 = True
jugador_x = ''
jugador_o= ''
turno = 0
jugada = 0

while turno < 9:
    if jugador_x == '':
        nombre_1 = input('\nNombre del primer jugador: ')
        opcion_1 = input('\nMuy bien ' + nombre_1 + ' ¿Deseas jugar como cruz (x) o como circulo (o)?: ')
        while opcion_1 != 'x' and opcion_1 != 'X' and opcion_1 != 'o' and opcion_1 != 'O':
            opcion_1 = input('\nPor favor, seleccione cruz (x) o circulo (o): ')
        if opcion_1 == 'x':
            jugador_x = nombre_1
            jugador_o = input ('\nNombre del segundo jugador (o): ')
        else:
            jugador_o = nombre_1
            jugador_x = input ('\nNombre del segundo jugador (x): ')
        print('\nLas posiciones se tienen en cuenta de acuerdo al pad numérico del teclado de la computadora')
        print('Ejemplo:')
        imprimir_tablero(ejemplo)
        print('\n¡'+ jugador_x + ' y ' + jugador_o + ' van van a jugar!\n')
        imprimir_tablero(tablero)
    else:
        if turno_1:
            jugada = int(input('\n' + jugador_x + ', elegí una posición: '))
        else:
            jugada = int(input ('\n' + jugador_o + ', elegí una posición: '))

        valor = cambiar_tablero(tablero, jugada, turno_1)
        if valor == 0:
            turno_1 = not turno_1
            turno += 1
            imprimir_tablero(tablero)
            if hay_ganador(tablero) == 1:
                print('\n' + jugador_x + " gano!")
                break
            elif hay_ganador(tablero) == 2:
                print('\n' + jugador_o + " gano!")
                break
        else:
            print(valor)

        if turno == 9:
            print ("\n¡Empate!")