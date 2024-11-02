import numpy as np

# a. Criação da matriz A com valores inteiros randômicos
A = np.random.randint(0, 100, (10, 10))  # Valores entre 0 e 99

# Impressão da matriz A
print("Matriz A:")
print(A)


# Impressão da soma de todos os valores da matriz A
soma_A = np.sum(A)
print("Soma de todos os valores da matriz A:", soma_A)

# b. Criação da matriz B onde cada item é o valor da matriz A * 3
B = A * 3

# Impressão da matriz B
print("Matriz B:")
print(B)