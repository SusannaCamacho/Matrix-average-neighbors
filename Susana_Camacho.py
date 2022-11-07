import numpy as np

def process_elements(process_neighbors):
    """
    Recibe una lista con el elemento y sus correspondientes vecinos. Calcula el promedio.
    """
   
    return round(sum(process_neighbors) / len(process_neighbors), 2)

def process_matrix(matriz):
    """
    Recibe una matriz, evalua los vecinos que tiene cada elemento, los añade a una nueva lista junto al valor de sí mismo y te devuelve la nueva matriz 
    """
    # Crear una nueva matriz del mismo tamaño que la matriz que recibimos, y la llena de 0
    new_matrix = np.zeros(shape=(len(matriz), len(matriz)))
    print(matriz)

    # Buscar los vecinos (i=fila=lista, j=columna=índice) y añadirlos a una nueva lista
    # Para cada elemento de la lista
    for i in range(len(matriz)):
        for j, number in enumerate(matriz[i]):
            # ver si se trata de un borde (i: primera o última fila de la matriz, j: primera o última posición del elemento en la lista)
            if i == 0 or i == len(matriz) - 1 or j == 0 or j == len(matriz[i]) - 1:
                process_neighbors = []
                # Ver qué vecinos (izq,derecha,arriba,abajo) hay que añadir a la lista
                if j != 0:
                    process_neighbors.append(matriz[i][j - 1]) # añade vecino de la izquierda
                if j != len(matriz[i]) - 1:
                    process_neighbors.append(matriz[i][j + 1]) # añade vecino de la derecha
                if i != 0:
                    process_neighbors.append(matriz[i - 1][j]) # añade vecino de arriba
                if i != len(matriz) - 1:
                    process_neighbors.append(matriz[i + 1][j]) # añade vecino de abajo

            else:
                # Añadir los 4 vecinos(izq,derecha,arriba,abajo)
                process_neighbors = [
                    matriz[i][j - 1], # vecino izquierda
                    matriz[i][j + 1], # vecino derecha
                    matriz[i - 1][j], # vecino arriba
                    matriz[i + 1][j] # vecino abajo
                ]

            # Una vez tenemos los vecinos de cada elemento, hay que añadir el propio elemento a la lista
            process_neighbors.append(number)
            
            # Llamamos a la función process_elements para que haga el promedio con el elemento y sus vecinos
            # Nos devuelve el promedio y ponemos ese resultado en su misma posición dentro de la matriz llena de ceros
            new_matrix[i][j] = process_elements(process_neighbors)
    print(new_matrix)

    return new_matrix

# TEST
#if __name__ == "__main__":
    print(process_matrix(np.random.randint(1, 10, size=(4, 4))))