estudiantes = []
bandera = True
id = 0
while bandera:

    id  = id + 1
    codigo = input("Ingrese el código del estudiante:")
    nombre = input("Ingrese el nombre del estudiante:").lower()
    tamaNotas = int(input("Ingrese el número de notas totales (la última nota es la convocatoria):"))
    notas = []
    for i in range(tamaNotas):
        n = float(input("Ingrese la nota numero "+str(i+1)+": "))
        notas.append(n)

    numNotas = len(notas) - 1

    notaSum = 0
    for a in range(numNotas):
        nota1 = notas[a]
        notaSum = notaSum + nota1
        
    p1 = (notaSum / numNotas) * 0.60
    p2 = (notas[numNotas]) * 0.40
    promedio = p1 + p2

    estudiantes.append([id,codigo, nombre, notas, promedio])
    
    addOther = "true"
    while addOther != "si" and addOther != "no":
        print("---------------------------------")
        addOther = input("Desea agregar otro estudiante? si/no :").lower()

        if addOther == "si":
            print("---------nuevo estudiante---------")
        elif addOther == "no":
            print("---------------------------------")
            bandera = False
        else:
            print("Ingrese una opcion valida")

total = len(estudiantes)
print("Ficha     Código     Nombres y apellidos")
for x in range(total):
    print (estudiantes[x])