nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


#ejercicio a

alumnos= nombres.replace(" " ,"").split(",")
alumnos_notas = {}

for i in range(len(alumnos)):

    alumnos_notas[alumnos[i]]= [notas_1[i],notas_2[i]]

for i in range(len(alumnos)):
    
    print(alumnos[i],":",alumnos_notas[alumnos[i]])
    
#ejercicio b
    
promedio = [(val[0]+val[1])/2 for key, val in alumnos_notas.items()]
 
for i in range(len(alumnos)):

    alumnos_notas[alumnos[i]].append(promedio[i])

print("\n")

print("La lista de los alumnos con sus notas y promedios es:")  

print("\n")    

for i in range(len(alumnos)):
    
    print(alumnos[i],":",alumnos_notas[alumnos[i]])

print("\n")

#ejercicio c

promedio_general = sum([(val[0]+val[1])/2 for key, val in alumnos_notas.items()])/len(alumnos_notas)

print(f"El promedio general es {promedio_general}"[:29])      

print("\n") 

#ejercicio d 

maximo = sorted(alumnos_notas.items(), key=lambda promedio: promedio[1][2], reverse = True)

print(f"La persona con mayor promedio es {maximo[0][0]} y su promedio es {maximo[0][1][2]}")

print("\n")

#ejercicio e

minimo = min(alumnos_notas[alumnos[0]])

for i in range(len(alumnos_notas)-1):

    if min(alumnos_notas[alumnos[i]]) < minimo:
    
        persona = alumnos[i]
        
        minimo = min(alumnos_notas[alumnos[i]])

print(f"La persona con la nota mas baja es {persona} y su nota es {minimo}")      





