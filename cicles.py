print("="*50)
print("||          REVICION DE TUS CALIFICACIONES      ||")
print("="*50 )


while True:
    finalGrade = input("Intoduce la nota final en un rango del (0 a 100): ").strip()
    try: 
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
         
     
grades = []
while True:
    inputGrade = input("Introduce las calificaciones en un rango del (0 a 100): ").split(",")
    try:
        for eachGrade in inputGrade:
            wrongValue = eachGrade
            if 0 < float(eachGrade) <= 100:
                    grades.append(float(eachGrade))
            else:
                print(f"La calificacion ingresada ({wrongValue}) esta fuera del rango, favor intentelo nuevamente")
                break 
        else:
             break
    except:
        print(f"ERROR: El valor ({wrongValue}) contiene letras o caracteres especiales")
        print(f"Datos correctos ({grades})")
        print(f"Favor continuar desde el ultimo valor ingresado: {grades[-1]})")

        

for x in grades: 
    val = sum(grades)/len(grades)
    print(f"{round(val,2)}")
    break

x=0
count=0
while True:
    specificValue = input("Introduce una calificacion especifica: ").strip()
    try: 
        vlSpecificValue = float(specificValue)                     
        if vlSpecificValue == grades[x-1]:
            repetitive += 1
        if vlSpecificValue >= grades[x-1]:
            count = count + 1 
        elif x >= len(grades):
            print(x)
            x += 1
        break        
        
    except:
        print(f"ERROR: el valor ingresado ({specificValue}) contiene letras o caracteres especiales, favor intentelo nuevamente\n")
        
print(grades)
   
   