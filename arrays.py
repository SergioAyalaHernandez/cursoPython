# Introducción a listas

array = ["futbol", "Pc", 18.5,18,[1,2,3,4],True,False, "Pc"]

# imprimir todo el array
print(array)

# imprimir un boolean como resultado de una busqueda
print("Pc" in array)

# imprimir el index de una busqueda en una lista, arroja el primer lugar donde lo encuentra
print(array.index("Pc"))

# contar un elemento o varios de una lista
print(array.count(1))
print(array.count("Pc"))
print(array.count("Hola"))
print(array.count(True))

# eliminar valores de una lista, elimina el primer valor que encuentre 
array.remove("Pc")
print(array)

# agregar valores al final de la lista
array.append("Pc")
print(array)

# agregar valores en un index a la lista
array.insert(1,"Hola Prros")
print(array)


