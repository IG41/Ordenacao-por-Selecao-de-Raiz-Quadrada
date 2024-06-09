📚 README: Ordenação por Seleção de Raiz Quadrada:

## 🚀 Introdução

Este projeto apresenta duas implementações de algoritmos de ordenação que utilizam a técnica de divisão e conquista baseada na raiz quadrada do tamanho do array. Os algoritmos são:

Ordenação por Seleção de Raiz Quadrada (Quadrática)
Ordenação por Seleção de Raiz Quadrada usando Heap

## 📜 Explicação do Código
 
 # 🛠 Ferramentas Utilizadas

Python: Linguagem de programação utilizada.
heapq: Biblioteca para manipulação de heaps em Python.
time: Biblioteca para medir o tempo de execução.
numpy: Biblioteca para geração de números aleatórios.

## 📊 Complexidade

Ordenação por Seleção de Raiz Quadrada (Quadrática): Este método utiliza a ordenação por bolha (bubble sort) para ordenar cada sub-vetor, resultando em uma complexidade O(n * sqrt(n)).
Ordenação por Seleção de Raiz Quadrada usando Heap: Este método utiliza heaps para gerenciar os sub-vetores ordenados, resultando em uma complexidade O(n log(sqrt(n))).

## 📝 Funções

sqrt_sort_quadratic(array)
Esta função ordena um array utilizando a técnica de divisão e conquista, onde:

Divide o array original em partes de tamanho igual à raiz quadrada do comprimento do array.
Ordena cada parte utilizando o algoritmo de ordenação por bolha.
Combina as partes ordenadas em um vetor auxiliar.
Complexidade: O(n * sqrt(n))

bubble_sort(arr)
Função auxiliar que implementa o algoritmo de ordenação por bolha para ordenar uma lista.

sqrt_sort_heap(array)
Esta função ordena um array utilizando heaps para gerenciar os sub-vetores ordenados, onde:

Divide o array original em partes de tamanho igual à raiz quadrada do comprimento do array.
Ordena cada parte utilizando a função sorted.
Utiliza um heap para combinar as partes ordenadas em um vetor auxiliar.
Complexidade: O(n log(sqrt(n)))

criar_entrada(n)
Função que cria uma entrada aleatória de tamanho n.

## 🔧 Execução

Exemplo de Uso
python
Copiar código
import numpy as np
import time

# Criar uma lista de entrada
lista1 = criar_entrada(10000001)

# Array de exemplo
array = [8, 11, 6, 4, 12, 7, 5, 15, 17, 1, 2]
print("Array original:", array)

# Ordenação por seleção de raiz quadrada (quadrática)
start_time = time.time()
result_quadratic = sqrt_sort_quadratic(lista1)
print(f"Tempo (Quadrático): {time.time() - start_time} segundos")

# Ordenação por seleção de raiz quadrada usando heap
start_time = time.time()
result_heap = sqrt_sort_heap(lista1)
print(f"Tempo (Heap): {time.time() - start_time} segundos")

## 🔍 Detalhes de Implementação

Divisão em Partes: Ambos os algoritmos dividem o array em sub-vetores de tamanho raiz quadrada do comprimento do array.
Ordenação das Partes: A ordenação das partes é feita utilizando diferentes métodos: ordenação por bolha para o método quadrático e sorted para o método heap.
Combinação dos Resultados: No método quadrático, os elementos são combinados sequencialmente. No método heap, um heap é utilizado para obter o próximo menor elemento de todos os sub-vetores.

🔗 Referências:

heapq
numpy

📧 Contato:

Para dúvidas ou sugestões, entre em contato através do GitHub https://github.com/IG41.
