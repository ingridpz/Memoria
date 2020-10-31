# A00826973 Ingrid Giselle Paz Ramírez
# A00827533 Leo Abraham Puente Rangel
# Fecha de entrega: 30/10/202
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
#Imagen
tiles = list(range(32)) * 2
#Número de parejas
#Si se desea utilizar letras en vez de números
#def letras(inicio, fin):
#     for x in xrange(ord(inicio), ord(fin)):
#          yield chr(x)
#tiles2 = []
#for a in letras('a', 'x'):
#      tiles2 = tiles2 + a
#La lista llega hasta x para que el tablero sea cuadrado
#el tablero será más pequeño.
state = {'mark': None}
#Indica el estado de las fichas
hide = [True] * 64
#Esconder la imagen
count = 0
#Puntaje

def square(x, y):
    #Dobuja el tablero
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    #Indice de las fichas
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    #Coordenadas de las fichas
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
       
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        

def draw():
    #Muestra la imagen 
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            

    mark = state['mark']

    if mark is not None and hide[mark]:
        #Escribe los números
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done
