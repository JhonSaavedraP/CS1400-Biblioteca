# ================================
# Proyecto: Dibujar una tarta con Turtle
# ================================
# En este ejercicio vas a:
# 1. Usar trigonometría para calcular la base de un triángulo isósceles.
# 2. Dibujar un triángulo con turtle.
# 3. Repetir el triángulo varias veces para formar una "tarta".
#
# ¡Lee cada paso con atención y completa los TODO!

# Importaciones necesarias
import math
import turtle

t = turtle.Turtle()
t.speed(0)

def triangulo(longitud, angulo):
    """
    TODO Paso 1:
    Escribe aquí qué hace esta función.
    
    Pista:
    - ¿Qué representa 'longitud'?
    - ¿Qué representa 'angulo'?
    - ¿Qué debería dibujar esta función?
    """
    
    # --------------------------------
    # Paso 2: Cálculos matemáticos
    # --------------------------------
    
    # Convierte el ángulo a radianes para poder usar funciones trigonométricas.
    angulo_rad = math.radians(angulo)
    
    # TODO:
    # Calcula la longitud de la base del triángulo isósceles.
    # Pista: estás trabajando con dos lados iguales (longitud)
    # y el ángulo central entre ellos.
    # Puedes usar math.sin().
    base = 2 * longitud * math.sin(angulo_rad / 2)
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.
    angulo_esquina = (180 - angulo) / 2

    # --------------------------------
    # Paso 3: Dibujo del triángulo
    # --------------------------------
    
    # Dibuja el triángulo usando forward() y left().
    # Recuerda:
    # - Debes dibujar dos lados iguales (longitud).
    # - Debes dibujar la base.
    # - La tortuga debe volver al punto inicial.
    
    t.forward(longitud)          
    t.left(180 - angulo_esquina) 
    t.forward(base)              
    t.left(180 - angulo_esquina) 
    t.forward(longitud)          
    t.left(180)                  
    
    # TODO:
    # Escribe aquí los movimientos necesarios.
    
    # pass  # ⚠️ Borra esta línea cuando completes el código


def dibujar_tarta(n_porciones, longitud):
    """
    TODO:
    Explica qué hace esta función.
    
    Pista:
    - ¿Qué es n_porciones?
    - ¿Qué representa longitud?
    """
    
    # --------------------------------
    # Paso 4: Calcular el ángulo de cada porción
    # --------------------------------
    
    # TODO:
    # Calcula el ángulo central de cada porción.
    # Pista: un círculo completo tiene 360 grados.
    angulo_porcion = 360 / n_porciones
    
    # --------------------------------
    # Paso 5: Dibujar todas las porciones
    # --------------------------------
    
    # TODO:
    # Escribe un bucle for que:
    # 1. Llame a la función triangulo(...)
    # 2. Gire la tortuga el ángulo necesario
    #    para dibujar la siguiente porción.
    
    # for ...:
    #     triangulo(...)
    #     left(...)
    
    direccion_inicial = t.heading() #Usamos .heading() para guardar el número de grados actual
    
    #Forzamos a la tortuga a apuntar al ángulo exacto por que antes la segunda tarta no se hacia correctamente. 
    
    for i in range(n_porciones):
        t.setheading(direccion_inicial + (i * angulo_porcion))
        triangulo(longitud, angulo_porcion)
    
    # pass  # ⚠️ Borra esta línea cuando completes el código



# ==================================
# Bloque para probar la función
# ==================================

ventana = turtle.Screen()
ventana.setup(600,400)

# ----------------------------------
# Prueba 1
# ----------------------------------

print("Dibujando una tarta de 5 porciones...")
t.penup()
t.goto(100, 0) # Posición para la primera tarta
t.pendown()
print("Dibujando una tarta de 5 porciones...")
dibujar_tarta(5, 80)

# ----------------------------------
# TODO EXTRA
# ----------------------------------
# 1. Levanta el lápiz (penup()).
# 2. Muévete a otra posición.
# 3. Baja el lápiz (pendown()).
# 4. Dibuja otra tarta con diferentes valores.



# ----------------------------------
# Prueba 2
# ----------------------------------

print("Dibujando una tarta de 8 porciones...")
t.penup()
t.goto(-150, 0) # Nos movemos para que no se encima
t.pendown()
print("Dibujando una tarta de 8 porciones...")
dibujar_tarta(8, 80)


turtle.done()