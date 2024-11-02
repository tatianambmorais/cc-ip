# Criar uma lista para armazenar os números
lista_de_numeros = []
for i in range(10):
    numero = input('Digite um novo número: ')
    lista_de_numeros.append(numero)
    print(lista_de_numeros)

# Verificar números repetidos e suas posições
numeros_repetidos = {}

for i in range(len(lista_de_numeros)):
    numero = lista_de_numeros[i]
    if numero in numeros_repetidos:
        numeros_repetidos[numero].append(i)  # Adiciona a posição se já existir
    else:
        numeros_repetidos[numero] = [i]  # Cria uma nova entrada

# Exibir os números repetidos e suas posições
tem_repeticao = False
for numero, posicoes in numeros_repetidos.items():
    if len(posicoes) > 1:  # Verifica se o número se repete
        tem_repeticao = True
        print(f'O número {numero} se repete nas posições: {posicoes}')

# Se não houver números repetidos
if not tem_repeticao:
    print('Não há números repetidos no vetor.')
