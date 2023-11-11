# Edgar Martínez Retes
# A01706825

'''

Este programa le da la opción al usuario de repasar python de tres distintas maneras. La primera es poder repasar el sintaxis de los diferentes temas
como condicionales y ciclos, primero con preguntas específicas y despues pidiendo al usario que escriba un código sencillo que cumpla con la
sintaxis. La siguiente opción es una serie de preguntas de opción múltiple de manera random, haciendo la cantidad de preguntas que le usuario
quiera. La última opción es un juego de ahorcado con las palabras reservadas de python para incluir el tema de los strings.

Para el tema de archivos de texto utilicé archivos csv(comma separated values) para una función de login, donde se pueden crear cuentas con nombre de usuario
y contraseña. El programa evalua si ese usuario existe para poder ingresar a las siguientes funciones.

'''

import random

import csv

# Función para verificar si la contraseña y el nombre están en el archivo

def verificar_cuenta(usuario, contraseña):
    # abrir el archivo en modo lectura
    with open("usuarios.csv", mode="r") as file:
        # el reader definirlo como dictreader(diccionario) para que pueda leer cada columna por sus nombres claves 
        reader = csv.DictReader(file)
        
        cuenta_valida = False
        for row in reader:
            # Cada linea evalua si el usuario y la contraseña coinciden con el inputt del usuario
            user = row['Usuario']
            password = row['Contraseña']
            if user == usuario and password == contraseña:
                cuenta_valida = True
                break
         
        if cuenta_valida == True:
            return True
        elif user == usuario:
            print("Contraseña incorrecta")
        else:
            print("Usuario o contraseña incorrecta")

def crear_cuenta():
    # Abrir un archico csv en modo escribir
    # Abrirlo en modo de a porque en w lo sobreescribe
    with open('usuarios.csv', mode='a') as file:
        # Se necesita un writer para poder escribir en el csv
        writer = csv.writer(file)
        # Escribir el usuario y la contraseña en el archivo
        usuario = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")
        nuevo = [usuario, contraseña]
        writer.writerow(nuevo)
        
#Función para el juego de ahorcado con strings

def ahorcado():
    
    #Elegir una palabra reservada random y guardarla en una variable adiconal para poder modificarla
    
    palabras = ["print", "if", "else", "break", "import", "def", "while", "for", "True", "False", "range", "len", "input", "int", "str", "and", "or", "not", "elif", "pass", "None", "continue", "return", "try", "del", "global", "except"]
    choice = random.randrange(0,len(palabras))
    palabra = palabras[choice]
    temp = palabra
    
    # Modificar la variable temporal para que solo salgan los espacios a llenar
    
    for i in range(len(temp)):
        temp = temp.replace(palabra[i], "_ ")
        
    print("")
    print(temp)
    
    #Número de intentos que se tienen
    
    intentos = 4
    x = 0
    
    while x < intentos:
        # Evalua si todavía faltan letras en la palabra
        if "_" in temp:
            print("")
            print("%i errores de 4" %x)
            print("")
            c = input("Adivina una letra o la palabra: ")
            # Evalua si se ingresó una letra o la palabra completa
            if len(c) == 1:
                # Si la letra está en en la palabra a adivinar realiza el ciclo. Se utiliza la función upper para evaluar minúsculas y mayúsculas por igual
                if c.upper() in palabra.upper():
                    # El ciclo busca todas las posiciones en la que la letra se encuentra
                    for j in range(len(palabra)):
                        # concatena la letra de la posición en su posición
                        if palabra[j].upper() == c.upper():
                            # se escribe del principio hasta una posición antes de la letra, luego la letra, luego desde una posición más de la lera hasta el final
                            temp = temp[:j*2] + palabra[j] + temp[(j*2)+1:]
                    print(temp)
                else:
                    print("Esa letra no está")
                    print("")
                    print(temp)
                    x += 1
            else:
                if c == palabra:
                    print("")
                    return "¡Esa es la palabra!"
                else:
                    print("")
                    return "No adivinaste la palabra. La palabra era: %s" %palabra
        else:
            print("")
            return "¡Esa es la palabra!"
    # si ya no hay más intentos        
    if x == 4:
        print("")
        return "4/4 intentos. No adivinaste la palabra. La palabra era: %s" %palabra
                
    
#Función para el repaso de lógica

def preguntas(n):
    
    #Guardar las preguntas y respuestas en una lista donde sus índices coincidan
    
    questions = ["Ciclo que se repite hasta que la condición se vuelva falsa:", "Ciclo que se repite una cantidad de veces definida:", "Palabra reservada para declarar una condición inicial:", "Nombre que se la da a una etiqueta que tiene un valor que puede cambiar:", "Nombre de la función que usualmente se le da al código principal:", "Valor que recibe una función:", 'Mensaje que no es leído por el programa y empieza con "#":', "Valor que solo puede ser verdadero o falso:", "Valor que solo son número enteros:", "Valor que son números con una parte decimal:", "Valor que es una cadena de caracteres:", "Pantalla donde se escriben entradas y se muestran las salidas:", "Elemento que puede guardar muchos valores con un órden específico:", "A una variable que define el número de veces que se repite el ciclo se le conoce como:", "A una variable que se actualiza cada vez que se le añade un valor se le conoce como:"]
    answers = ["while", "for", "if", "variable", "main", "parámetro", "comentario", "bool", "interger", "float", "string", "terminal", "lista", "contador", "acumulador"]
    repetidas = []
    
    aciertos = 0
    errores = 0
    
    print("")
    
    # Elegir una pregunta al azar. Si ya se hizo esta pregunta vuelve a elegir otra ahsta que sea una pregunta diferente.
    
    for i in range(n):
        while True:
            print("Pregunta %i: " % (i + 1), end = "")
            while True:
                choice = random.randrange(0,len(questions))
                if choice in repetidas:
                    continue
                else:
                    repetidas.append(choice)
                    print(questions[choice])
                    break
            print("")
            
            # Añade la respuesta a la pregunta en la lista de opciones que se van a desplegar
            
            opciones = []    
            opciones.append(choice)
            
            # Añade 3 opciones adicionales mientras no estén ya en la lista.
            
            for j in range(3):
                while True:
                    choice2 = random.randrange(0,len(answers))
                    if choice2 in opciones:
                        continue
                    else:
                        opciones.append(choice2)
                        break
                    
            # Crea una segunda lista con las opciones revueltas        
            opciones_2 = []
            for k in range(4):
                while True:
                    inciso = opciones[random.randrange(0, 4)]
                    if inciso in opciones_2:
                        continue
                    else:
                        opciones_2.append(inciso)
                        break
              
            # Despliega las opciones de la segunda lista de opciones  
              
            for l in range(4):
                print("%i. %s" %(l+1, answers[opciones_2[l]]))
              
            # Valida que el input sea un número entero entre 1 y 4
            
            while True:
                try:
                    inp = int(input("Respuesta: "))
                    if inp < 1 or inp > 4:
                        print("Respuesta inválida")
                        continue
                    break
                except ValueError:
                    print("Respuesta inválida")
                    continue
            
            # Si opciones2 con en la posición input es el mismo número de indice de la pregunat está correcta
            
            if choice == opciones_2[inp-1]:
                aciertos += 1
                print("¡Correcto!")
                print("")
            
            elif choice != opciones_2[inp-1]:
                errores += 1
                print("Respuesta incorrecta. \nLa respuesta era: %s" %(answers[choice]))
                print("")
            
            break
      
    print("¡Perfecto! Has terminado.") 
    print("")
    return aciertos, errores

# Función para la opción de ciclo_while

def ciclo_while():
    
    aciertos = 0
    errores = 0
    
    print("")
    print("Un ciclo while va a realizar las instrucciones dentro del ciclo mientras una condición se cumpla. Es decir, mientras cierto argumento sea verdadero, el ciclo se va a repetir hastq ue este argumento pase a ser falso")
    print("Para hacer un ciclo while, se utiliza un contador que va aumentando o disminuyendo cada ciclo para realizar las instrucciones una cantidad de veces específica. También se puede usar condicionales que cuando se cumpla cierto caso rompa el ciclo")
    print("")
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("while x > y:")
        print("")
        print("¿Qué se debe de hacer para que el ciclo no sea infinito?")
        print("1. Disminuir el valor de y")
        print("2. Repetir el ciclo las veces que indique x")
        print("3. Disminuir el valor de x")
        res_x = int(input("Respuesta: "))
        if res_x == 3:
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta")
            print("")
            continue

    # La pregunta se repite hasta que se de con la opción correcta

    while True:
        print('\nx = 7\ny = 3\nwhile x > y:\n\tprint(x, end=" ")')
        print("")
        print("¿Cuál es la salida de este ciclo?")
        print("1. 7 6 5 4 3")
        print("2. 7 7 7 7 7 7 ... 7 ...")
        print("3. 7 6 5 4")
        res_7 = int(input("Respuesta: "))
        if res_7 == 2:
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta")
            print("")
            continue
      
    # La pregunta se repite hasta que se de con la opción correcta
      
    while True:
        print('\nx = 7\ny = 3\nwhile x > y:\nprint(x, end=" ")\nx -= 1')
        print("")
        print("¿Cuál es el error en este código?")
        print("1. El contador no cambia y se hace un ciclo infinito")
        print("2. Las intrucciones no están dentro del while")
        print("3. y es mayor que x y nunca entra al ciclo")
        res_tab = int(input("Respuesta: "))
        if res_tab == 2:
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta")
            print("")
            continue
    print("")   
    print("!Muy bien! Ahora que ya conoces el funcionamiento de cada elemento de un ciclo while es tu turno de crear tu código")
    print('Escribe un código que imprima por la cantidad de veces que el usuario indique "¡Gol!"')
    print('Especificaciones:\n-La variable de la entrada tiene que llamarse "num" y el input no tiene valor entre los paréntesis\n-Los espacios, mayúsculas y minúsculas y tabulaciones tienen que coincidir con los ejemplos anteriores para coincidir con el programa\n-Las tabulaciones se ponen con 4 espacios\n-No se puede regresar a la línea anterior\n-Utilizar la variable "i" para el contador (i = 0)\n-El contador tiene que ser el número de elefantes que se imprima')
    print("")
    
    # Evalua el código escrito por el usuario línea por línea. Si el input no es igual a lo que debería de haber escrito se marca el error y se añade esa línea a la lista para desplegar las líneas donde hubo errores.

    while True:

        lineas = []
                    
        linea1 = input("|1|... ")
        if linea1 == "num = int(input())":
            aciertos += 1
        else:
            lineas.append(1)
            errores += 1
            
        linea2 = input("|2|... ")
        if linea2 == "i = 0":
            aciertos += 1
        else:
            lineas.append(2)
            errores += 1
            
        linea3 = input("|3|... ")
        if linea3 == "while i <= num:":
            aciertos += 1
        else:
            lineas.append(3)
            errores += 1
            
        linea4 = input("|4|... ")
        if linea4 == "    print(¡Gol!)":
            aciertos += 1
        else:
            lineas.append(4)
            errores += 1
            
        linea5 = input("|5|... ")
        if linea5 == "    i = i + 1" or linea5 == "    i += 1":
            aciertos += 1
        else:
            lineas.append(5)
            errores += 1
            
        print("")
        
        # Despliega en la pantalla el código correcto
                
        if len(lineas) > 0:
            print("Errores en las líneas: ", end = "")
            for i in range(len(lineas)):
                print(lineas[i], end = " ")
            print("\nEl código debió quedar así: ")
            print("")
            print('num = int(input())\ni = 0\nwhile i <= num:\n\tprint(¡Gol!)\n\ti += 1')
            otra = input("¿Intentar de nuevo? (S/N): ")
            print("")
            if otra == "S" or otra == "s":
                print("")
                continue
            else:
                print("")
                break
        print("¡Perfecto! Has terminado")    
        print("")
        break
    return aciertos, errores

def ciclo_for():
    
    aciertos = 0
    errores = 0
    
    print("")
    print("Para hacer un ciclo for necesitaremos ciertos elementos. Contesta las siguientes preguntas en relación a su sintaxis:")
    print("")
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("for i in range(3, 20, 2):")
        print("¿Qué representa la i?: ")
        print("1. Contador")
        print("2. Acumulador")
        print("3. Variable constante")
        res_i = int(input("Respuesta: "))
        if res_i == 1:
            aciertos += 1
            break
        else:
            print("Respuesta incorrecta")
            print("")
            errores += 1
            continue
        
    print("")
    
    # La pregunta se repite hasta que se de con la opción correcta
        
    while True:
        print("for i in range(2, 15):")
        print("¿Cuál es el rango de i?: ")
        print("1. (3, 14)")
        print("2. (2, 15)")
        print("3. (2, 14)")
        res_range = int(input("Respuesta: "))
        if res_range == 3:
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta")
            print("")
            continue
        
    print("")
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("for i in range(12, 4, -4):")
        print("¿Qué números imprimira este ciclo?: ")
        print("1. 12, 11, 10, 9, 8, 7, 6, 5")
        print("2. 12, 8")
        print("3. 12, 8, 4")
        res_serie = int(input("Respuesta: "))
        if res_serie == 2:
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta")
            print("")
            continue
        
    print("")
        
    print("!Muy bien! Ahora que ya conoces el funcionamiento de cada elemento de un ciclo for es tu turno de crear tu código")
    print("Escribe un código que pida un número al usuario y haga un ciclo la misma cantidad de veces que ese número - 1. En cada ciclo el número va a disminuir de dos en dos mientras que se va sumando el contador a un acumulador y lo va a imprimir al final")
    print('Especificaciones:\n-La variable de la entrada tiene que llamarse "num" y el input no tiene valor entre los paréntesis\n-Los espacios, mayúsculas y minúsculas y tabulaciones tienen que coincidir con los ejemplos anteriores para coincidir con el programa\n-Las tabulaciones se ponen con 4 espacios\n-No se puede regresar a la línea anterior\n-Utilizar la variable "i" para el contador"\n-Crear un acumulador en la primera línea de esta manera: acum = 0')

    print("")
    
    # Evalua el código escrito por el usuario línea por línea. Si el input no es igual a lo que debería de haber escrito se marca el error y se añade esa línea a la lista para desplegar las líneas donde hubo errores.
    
    while True:

        lineas = []
                
        linea1 = input("|1|... ")
        if linea1 == "acum = 0":
            aciertos += 1
        else:
            lineas.append(1)
            errores += 1
            
        linea2 = input("|2|... ")
        if linea2 == "num = int(input())":
            aciertos += 1
        else:
            lineas.append(2)
            errores += 1
            
        linea3 = input("|3|... ")
        if linea3 == "for i in range(0, num, 2):":
            aciertos += 1
        else:
            lineas.append(3)
            errores += 1
        
        linea4 = input("|4|... ")
        if linea4 == "    acum = acum + i" or linea4 == "    acum += i":
            aciertos += 1
        else:
            lineas.append(4)
            errores += 1
            
        linea5 = input("|5|... ")
        if linea5 == "print(acum)":
            aciertos += 1
        else:
            lineas.append(5)
            errores += 1
            
        print("")
            
        # Despliega el código correcto    
            
        if len(lineas) > 0:
            print("Errores en las líneas: ", end = "")
            for i in range(len(lineas)):
                print(lineas[i], end = " ")
            print("\nEl código debió quedar así: ")
            print("")
            print('acum = 0\nnum = int(input())\nfor i in range(0, num, 2):\n\tacum = acum + i\nprint(acum)')
            otra = input("¿Intentar de nuevo? (S/N): ")
            print("")
            # Estas condiciones permiten repetir el ejercicio si se pone "s"
            if otra == "S" or otra == "s":
                print("")
                continue
            else:
                print("")
                break
        print("")        
        break
    
    print("¡Perfecto! Has terminado")
    print("")
    return aciertos, errores

def condicionales():
    
    aciertos = 0
    errores = 0
    
    print("")
    print("En esta función el usuario da un valor de entrada (perro o gato) y va a validarlo para después imprimir el sonido de cada animal")
    print('animal = input("Perro/Gato: ")')
    print('if animal == "Perro" or animal == "perro": ')
    print('\tprint("Woof woof!")')
    print('elif animal == "Gato" or animal == "gato": ')
    print('\tprint("Miau!")')
    print('else:')
    print('\tprint("Ese animal no es una opción")')
    print("")
    
    print('Ahora es tu turno. Rellena los espacios de los elementos que faltan y encuentra que animales hacen los siguientes sonidos: "muuuu", "cricri"')
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("")
        print("¿Qué hace falta en el espacio en blanco?. ¿Cúal es la palabra designada para pedir una entrada al usuario?")
        print("")
        inpt = input('animal = ______("?/?: ") -> ')
        if inpt == "input":
            print("¡Muy bien!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta. Recuerda que se debe pedir una entrada al usuario")
      
    # La pregunta se repite hasta que se de con la opción correcta  
      
    while True:
        print("")
        print("¿Qué hace falta en el espacio en blanco? Recuerda que estás abriendo un condicional.")
        print("")
        si = input('___ animal == ... -> ')
        if si == "if":
            print("¡Muy bien!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta. Recuerda que hay palabras designadas para empezar un condicional")
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("")
        print("¿Qué hace falta en el espacio en blanco? Recuerda que estás creando un if anidado.")
        print("")
        sino = input('___ animal == ... -> ')
        if sino == "elif":
            print("¡Muy bien!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta. Recuerda que necesitas la palabra designada para ramificar el 'if'")
    
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("")
        print("¿Qué hace falta en el espacio en blanco? Recuerda que estás haciendo una condición si no se cumple ningún criterio.")
        print("")
        els = input('if...:\nelif...:\n_____: -> ')
        if els == "else":
            print("¡Muy bien!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Respuesta incorrecta. Recuerda que necesitas la palabra designada para los casos donde no se cumple ninguna condición")
            
    # La pregunta se repite hasta que se de con la opción correcta
    
    while True:
        print("")
        vaca = input("Ahora, ¿cuál es el primer animal (muuuu)?: ")
        if vaca == "Vaca" or vaca == "vaca":
            print("¡Una vaca!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Ese no es el animal")
            
   # La pregunta se repite hasta que se de con la opción correcta 
    
    while True:
        print("")
        grillo = input("¿Y cuál es el segundo animal (cricri)?: ")
        if grillo == "Grillo" or grillo == "grillo":
            print("¡Un grillo!")
            aciertos += 1
            break
        else:
            errores += 1
            print("Ese no es el animal")
            
    print("")
    print("Así quedó tu código:")
    print("")
    
    print("En esta función el usuario da un valor de entrada (perro o gato) y va a validarlo para después imprimir el sonido de cada animal")
    print('animal = input("Vaca/Grillo: ")')
    print('if animal == "Vaca" or animal == "vaca": ')
    print('\tprint("Muuuu!")')
    print('elif animal == "Grillo" or animal == "grillo": ')
    print('\tprint("Cricri")')
    print('else:')
    print('\tprint("Ese animal no es una opción")')
    print("")
    
    # Evalua el código escrito por el usuario línea por línea. Si el input no es igual a lo que debería de haber escrito se marca el error y se añade esa línea a la lista para desplegar las líneas donde hubo errores.
    
    while True:
        print('Es tu momento de crear tu propio código. Realiza un programa con estructura condicional que pida al usuario un número y verifique si este es par o no - print("Par"), print("Non"), print("Error")')
        print('Especificaciones:\n-La variable de la entrada tiene que llamarse "num" y el input no tiene valor entre los paréntesis\n-Los espacios, mayúsculas y minúsculas y tabulaciones tienen que coincidir con los ejemplos anteriores para coincidir con el programa\n-Las tabulaciones se ponen con 4 espacios\n-No se puede regresar a la línea anterior\n-Validar opciones inválidas')
        print("Comienza tu código: ")
        print("")
        
        lineas = []
            
        linea1 = input("|1|... ")
        if linea1 == "num = int(input())":
            aciertos += 1
        else:
            lineas.append(1)
            errores += 1
                
        linea2 = input("|2|... ")
        if linea2 == "if num%2 == 0:":
            aciertos += 1
        else:
            lineas.append(2)
            errores += 1
        
        linea3 = input("|3|... ")
        if linea3 == '    print("Par")':
            aciertos += 1
        else:
            lineas.append(3)
            errores += 1
            
        linea4 = input("|4|... ")
        if linea4 == 'elif num%2 != 0:':
            aciertos += 1
        else:
            lineas.append(4)
            errores += 1
            
        linea5 = input("|5|... ")
        if linea5 == '    print("Non")':
            aciertos += 1
        else:
            lineas.append(5)
            errores += 1
            
        linea6 = input("|6|... ")
        if linea6 == 'else:':
            aciertos += 1
        else:
            lineas.append(6)
            errores += 1
            
        linea7 = input("|7|... ")
        if linea7 == '    print("Error")':
            aciertos += 1
        else:
            lineas.append(7)
            errores += 1
        
        # Muestra el codigo que se debía de haber escrito
        
        if len(lineas) > 0:
            print("Errores en las líneas: ", end = "")
            for i in range(len(lineas)):
                print(lineas[i], end = " ")
            print("\nEl código debió quedar así: ")
            print("")
            print('num = int(input())\nif num%2 == 0:\n\tprint("Par")\nelif num%2 != 0:\n\tprint("Non")\nelse:\n\tprint("Error")')
            otra = input("¿Intentar de nuevo? (S/N): ")
            print("")
            #Opción para volverlo a intentar
            if otra == "S" or otra == "s":
                continue
            else:
                break
            
        break
    
    print("¡Perfecto! Has terminado")
    print("")
    
    return aciertos, errores

# Función que despliega el menú para ciclos

def ciclos():
    print("")
    print("1. For")
    print("2. While")
    print("3. Salir")
    print("")
            
# Función que despliega las opciones de repaso de temas

def sintaxis():
    print("")
    print("1. Condicionales")
    print("2. Ciclos")
    print("3. Salir")
    print("")

# Función que despliega el menú principal

def menu():
    print("")
    print("1. Sintaxis")
    print("2. Lógica(Preguntas de teoría)")
    print("3. Palabras reservadas (Ahorcado)")
    print("4. Salir")
    print("")
    
def menu2():
    print("")
    print("1. Ingresar")
    print("2. Crear cuenta")
    print("3. Salir")
    print("")
    
def existencia():
    
    # SI el archivo existe la función regresa True. Si no existe, el error que sale al no encontralo regresa False
    try:
        with open("usuarios.csv", mode="r") as file:
            return True
    except FileNotFoundError as x:
        return False
    except IOError as x:
        return False
    
def main():
    print("Bienvenido a mi programa para aprender python")
    
    # Se repite hasta que el usuario seleccione la opción de salir
    while True:
        # Una función para saber si el archivo ya existe y no sobreescribirlo. Si no existe, regresa False y lo crea
        found = existencia()
        
        if found == False:
            fields = ["Usuario", "Contraseña"]
            with open('usuarios.csv', mode='w') as file:
                # Se necesita un writer para poder escribir en el csv
                writer = csv.writer(file)
                # Definir las columnas
                writer.writerow(fields)
            
        menu2()
        acceso = int(input("Si tienes una cuenta selecciona ingresar. Si aún no tienes, crea tu cuenta: "))
        print("")
        if acceso == 1:
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            found = verificar_cuenta(usuario, contraseña)
            # Si ingreso un usuario existente y la contraseña correcta corre todo el código
            if found == True:
                print("")
                print("Ingreso exitoso")
                print("")
                # Se repite hasta que el usuario quiera terminar
                while True:
                    menu()
                    opcion = int(input("¿Qué te gustaría repasar?: "))
                    # Opción de sintaxis. Despliega los temas que puedes repasar
                    if opcion == 1:
                        # Se repite hasta que el usuario seleccione la opción de salir
                        while True:
                            sintaxis()
                            opcion_2 = int(input("¿Cuál de estos temas deseas repasar?: "))
                            # Opción de condicionales
                            if opcion_2 == 1:
                                aciertos, errores = condicionales()
                                print("SINTAX CONDICIONALES\nAciertos: %i\nErrores: %i" %(aciertos, errores))
                            # Opción de ciclos
                            elif opcion_2 == 2:
                                # Se repite hasta que el usuario seleccione salir
                                while True:
                                    ciclos()
                                    opcion_3 = int(input("Practicar ciclo for o while: "))
                                    # Opción de for
                                    if opcion_3 == 1:
                                        aciertos, errores = ciclo_for()
                                        print("SINTAX CICLO FOR\nAciertos: %i\nErrores: %i" %(aciertos, errores))
                                    # Opción de while
                                    elif opcion_3 == 2:
                                        aciertos, errores = ciclo_while()
                                        print("SINTAX CICLO WHILE\nAciertos: %i\nErrores: %i" %(aciertos, errores))
                                    # Opción para salir de la sección de ciclos
                                    elif opcion_3 == 3:
                                        break
                                    # Opción para validar solamente las opciones disponibles
                                    else:
                                        print("Opción inválida. Seleccione un número de opción")
                            # Opción para salir de la sección de repasar los temas
                            elif opcion_2 == 3:
                                break
                            else:
                                print("Opción inválida. Seleccione un número de opción")
                    # Opción para la selección de preguntas            
                    elif opcion == 2:
                        qs = int(input("¿Cuántas preguntas quieres hacer? El límite es 10: "))
                        # Evalua que el usuario solamente ponga hasta 10 preguntas
                        if qs > 0 and qs <= 10:
                            aciertos, errores = preguntas(qs)
                            print("PREGUNTAS LÓGICA\nAciertos: %i\nErrores: %i" %(aciertos, errores))
                        else:
                            print("Ese número de preguntas no es válido")
                    # Opción para el ahorcado
                    elif opcion == 3:
                        msj = ahorcado()
                        print(msj)
                    # Opción para terminar el programa        
                    elif opcion == 4:
                        break
                    # Opción para validar solo los números válidos
                    else:
                        print("Opción inválida. Seleccione un número de opción")
        elif acceso == 2:
            crear_cuenta()
            print("Cuenta creada con éxito")
            print("")
        elif acceso == 3:
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida")
            print("")

main()

# Ejemplo casos de prueba

'''
Caso 1 (función de cuentas):
input: 1
input: Edgar
input: 123
output: Usuario o cotraseña incorrecta
input: 2
input: Edgar
input: 123
output: Cuenta creada con éxito
input: 1
input: Edgar
input: 123
output: Usuario exitoso


Caso 1 (después de ingresar):

input: 1
input: 4
output: Opción inválida. Seleccione un número de opción
input: 1
input: input
input: hwmhw
output: Respuesta incorrecta. Recuerda que hay palabras designadas para empezar un condicional
input: if
input: elif
input: else
input: caballo
output: Ese no es el animal
input: vaca
input: grillo
input: num = int(input())
       if num%2 == 0:
           print("Par")
       if num%2 != 0:
           print("Non")
       else:
           print("Error")
output: Errores en las líneas: 4
        El código debió quedar así:
        num = int(input())
        if num%2 == 0:
            print("Par")
        elif num%2 != 0:
            print("Non")
        else:
            print("Error")
        ¿Intentar de nuevo? (S/N):
input: s
input: num = int(input())
       if num%2 == 0:
           print("Par")
       elif num%2 != 0:
           print("Non")
       else:
           print("Error")        
output: ¡Perfecto! Has terminado
        SINTAX CONDICIONALES
        Aciertos: 19
        Errores: 3
input: 3
input: 3
output: ¡Hasta pronto!

Caso 2:

input: 2
input: 3
output: Pregunta 1: Valor que solo son número enteros:
        1. main
        2. lista
        3. interger
        4. bool
input: 3
output: ¡Correcto!
output: Pregunta 2: Nombre que se la da a una etiqueta que tiene un valor que puede cambiar:
        1. while
        2. float
        3. for
        4. variable
input: 1
output: Respuesta incorrecta.
        La respuesta era: variable
output: Pregunta 3: Nombre de la función que usualmente se le da al código principal:
        1. for
        2. if
        3. main
        4. contador
input: 3
output: ¡Correcto!
output: ¡Perfecto! Has terminado
        PREGUNTAS LÓGICA
        Aciertos: 2
        Errores: 1
input: 3
output: ¡Hasta pronto!


'''