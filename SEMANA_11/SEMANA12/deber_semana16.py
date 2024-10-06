# paso 1 crear un  archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# paso2 Escribe al menos tres líneas de notas personales en el archivo
my_notes.write("Línea 1: Hola mi nombre es Edison Logacho Tobar.\n")
my_notes.write("Línea 2: Soy de la cuidad de Quito,un cuidad linda en todo el sentido de la palabra .\n")
my_notes.write("Línea 3: Estudio en la Universidad Estal Amazónica .\n")
# paso3 Lee el contenido del archivo línea por línea utilizando el método adecuado.
lineas = ["Línea 4: Tengo 40 años.\n", "Línea 5: Soy casado y tengo dos hijos varones.\n"]
my_notes.writelines(lineas)

my_notes.close()

# paso4 Abrir el archivo my_notes.txt y leer los archivos.
my_notes = open('my_notes.txt', 'r')

#Lee el contenido del archivo línea por línea utilizando el método adecuado.

# Método 1. read()
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
# cerrar el archivo
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()