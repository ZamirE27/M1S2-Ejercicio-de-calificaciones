print("="*50)
print("||          REVICION DE TUS CALIFICACIONES      ||")
print("="*50 )

print("="*50)
print("||              APROVADO/REPROBADO              ||")
print("="*50 )

# empezamos usando while para solicitar un dato y si no cumple las validaciones lo solicite nuevamente
while True: 
    finalGrade = input("Intoduce la nota final en un rango del (0 a 100): ").strip() # ingresa como str 
    try: # Usamos Try para poder atrapar el error y por medio del except ser mostrado en pantalla
        vlfinalGrade = float(finalGrade)   
        if 0 < vlfinalGrade <= 100:
            if vlfinalGrade >= 60:
                print(f"'FELICITACIONES' has aprovado la materia con: {vlfinalGrade}")
                break   
            else:
                print(f"'REPROBADO' has reprobado la materia con: {vlfinalGrade}")
                break    
        else:
            print("ERROR: el valor ingresado esta fuera del rango, favor intentelo nuevamente")
            
    except:
        print(f"ERROR: el valor ingresado ({finalGrade}) contiene letras o caracteres especiales, favor intentelo nuevamente\n")

print("="*50)
print("||           PROMEDIA TUS CALIFICACIONES        ||")
print("="*50) 
         
# Creamos una lista o array que almacenara todos los datos ingresados 
grades = [] 
while True:
    inputGrade = input("Introduce las calificaciones en un rango del (0 a 100) y separalas por comas (','): ").split(",") # Esta es una lista temporal que nos almacenara los datos ingresado en str 
                                                                                    # por medio del .split(,) nos aseguramos que los dats ingresados en el array se distingan o separen por una coma para asi almacenarlos individualmente.
    try:
        # Usamos un for para recorrer la lista y que el identador auma y almacene el valor del dato ingresado, el cual convertiremos a un float()
        for eachGrade in inputGrade:
            wrongValue = eachGrade
            if 0 < float(eachGrade) <= 100:
                    grades.append(float(eachGrade)) # Usando el .append() guardamos los datos ingresados en la lista temporal y recorridos y almacenados por el identador en la lista definida por fuera del while.
            else:
                print(f"La calificacion ingresada ({wrongValue}) esta fuera del rango, favor intentelo nuevamente")
                break 
        else:
             break
    except:
        print(f"ERROR: El valor ({wrongValue}) contiene letras o caracteres especiales")
        print(f"Datos correctos ({grades})")
        if grades: # Utilizamos este condicional para validar que si la lista no esta vacia nos imprima el valor alli, esto para evitar un error general del codigo en unos de los condicionales anteriores.
            print(f"Favor continuar desde el ultimo valor ingresado: {grades[-1]})")
# Caculamos el promedio utlizando la funcion sum() y dentro de esta ponemos la lista para sumar los valores entre si, y posterios a esto los dividimos entre len(grades) lo que significa el numero de posiciones dentro del array.
Average = sum(grades)/len(grades)
print(f"EL promedio de tus calificaciones es: {round(Average,2)}\n") # :round() se usa para redondear un valor float

print("="*50)
print("||       CALIFICACIONES MAYORES E IGUALES       ||")
print("="*50) 
breaker = True

repetitive=0
count=0
amount = 0      
eachG = 0

# Solicitamos el ingreso de una calificacion ya especifica y validamos nuevamente usando while, try: except:
while breaker == True:
    specificValue = input("Introduce una calificacion especifica dentro de las ya insgredas anteriormente: ").strip()
    try: 
        vlSpecificValue = float(specificValue) 
        if 0 < vlSpecificValue <= 100:
            if vlSpecificValue in grades:
                breaker = False

                # Con este loop while condicionado a repetirse mientras el Indice sea menor a la longitud de la lista
                # Y si el valor que esta en la lista (Grades) en la posicion (eachG) = indice es mayor que el dato ingresado entonces el contador (amount)se sumara una vez el indice aumentara una posicion 
                while eachG < len(grades):
                    if grades[eachG] > vlSpecificValue:
                        amount += 1
                    eachG += 1
                print(f"Hay {amount} calificaciones mayores a {vlSpecificValue}")      

                # Usamos loop for, para recorrer la lista y condicionamos a que cada que el indentador sea = al dato solicitado 
                # el contador sumara 1, una vez termine la lista tendremos cuantas veces se repitio el dato ingresado
                for repeated in grades:
                    if repeated == vlSpecificValue :
                        count += 1
                if count == 1:
                    print(f"La calificacion: {vlSpecificValue} se repite {count} vez)")
                else:
                    print(f"La calificacion: {vlSpecificValue} se repite {count} veces)")    
                """
                # este while se uso para validar cuantas vesces se repite un numero dentro de la lista, sin embargo el ejercicio solicito un loop for.
                while True:    
                    if vlSpecificValue == grades[count-1]:
                        repetitive += 1
                    if count+1 > len(grades):
                        print(f"La calificacion: {vlSpecificValue} se repite {repetitive} veces")
                        break
                    count +=1
                """    
            else:
                print(f"ERROR: El valor ({vlSpecificValue}) no coincide con ningun valor ingresado anteriormente")
                     
        else:
            print(f"ERROR: El valor ({vlSpecificValue}) esta fuera del rango permitido") 
            
    except:
        print(f"ERROR: el valor ingresado ({specificValue}) contiene letras o caracteres especiales")
