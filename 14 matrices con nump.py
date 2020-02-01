import numpy as np # SIEMPRE SE LLAMA A NUMPY
# https://numpy.org/doc/
unos = np.ones((3,4))
print(unos)

ceros = np.zeros((30,40))
print(ceros)



aleatorios = np.random.random((2,2))
print(aleatorios)

vacia=np.empty((3,2))
print(vacia)


full = np.full((20,2),2)
print(full)


# se desea crear una matriz con valores esoaciados uniformemente
espacios1 = np.arange(0,31,5)
print(espacios1)

# matriz con valores que se encuentren entre 0 y 2
espacios2 = np.linspace(0,2,10)
print(espacios2)


# crea matrices de identidad

identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(8)
print(identidad2)
# muestra la dimension de la matric
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print(a.shape)


# conoce el tipo de datos
a = np.array([(1,2,3)])
print(a.dtype)


# conocer el tamaño y forma de la matriz
a = np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

# cambio de forma d euna matriz = no e si giaul a trasnponer
a = np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

a = np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1) # espaciado
print(a[1,2])

print(a.min())
print(a.max())
print(a.sum())

#raiz acuadrada y desciacion estanbar
b=a
a
print(np.sqrt(a))
print(np.std(a))
# operaciones con matrices
print(a-9*b)
