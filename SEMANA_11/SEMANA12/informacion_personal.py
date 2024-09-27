#1 crear un diccionario
persona ={
    "nombre":"Edison",
    "apellido":"Logacho ",
    "edad": "40",
    "ciudad": "Quito",
}
#obtener los valores
print("nombre :",persona["nombre"])
print("apellido :",persona["apellido"])
print("edad :",persona["edad"])
print("cuidad :",persona["ciudad"])
#2 modificar clave
persona["cuidad"]="Cuenca"
print("nombre :",persona["nombre"])
print("apellido :",persona["apellido"])
print("edad :",persona["edad"])
print("ciudada :",persona["ciudad"])
#agregar un par clave
persona["profeción"]="Arquitecto"
print("todo :",persona)
#verificar si existe una clave
print("teléfono" in persona )
#agregar número telefónico
persona["teléfono"]= "0992725478"
print("todo :",persona)
#4 eliminar una clave
del persona["edad"]
print("todo :",persona)
#imprimir solo claves
claves = persona.keys()
print("claves :",claves)
#imprimir valores
valores = persona.values()
print("valores :",valores)
#recorrer como for
for claves,valores in persona.items():
    print(claves," : ",valores)
