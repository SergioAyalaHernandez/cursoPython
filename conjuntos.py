A = {1,2,3,4}
B = {2,3,5,6}
C = {3,4,6,7}

# comparación de resultados

# COmparación exacta
print(A==B)

# Union de conjuntos no deja repetidos, deja solo los datos que sean únicos
print(A | B)
print(A | C)
print(A | B | C)


# intercecciones entre conjuntos
print(A&C)
print(A&B)

# Diferencia de conjuntos, datos que tenga el conjunto en la izquierda y no el de la derecha
print(A-B)

# Diferencia simétrica, deja los datos que no se repiten entre los conjuntos
print(A^B)

