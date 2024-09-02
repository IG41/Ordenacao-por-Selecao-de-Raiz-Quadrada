import heapq
import time


def sqrt_sort_quadratic(array):
  n = len(array)
  sqrt_n = int(n**0.5)

  parts = [array[i:i + sqrt_n] for i in range(0, n, sqrt_n)]

  for part in parts:
    bubble_sort(part)

  aux_vector = []

  while parts:
    max_val = float('-inf')
    max_index = -1

    for i, part in enumerate(parts):
      if part[-1] > max_val:
        max_val = part[-1]
        max_index = i

    aux_vector.append(max_val)

    parts[max_index].pop()

    if not parts[max_index]:
      parts.pop(max_index)

  return aux_vector


def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sqrt_sort_heap(array):
    sqrt_n = int(len(array) ** 0.5)
    parts = [array[i:i+sqrt_n] for i in range(0, len(array), sqrt_n)]

    aux_heap = []

    for index, part in enumerate(parts):
      heapq.heapify(part)
      heapq.heappush(aux_heap, (part[0], index))

    sorted_list = []

    while aux_heap:
      min_value, index_min_value = heapq.heappop(aux_heap)
      
      sorted_list.append(min_value)
      
      heapq.heappop(parts[index_min_value])
      if parts[index_min_value]:
        heapq.heappush(aux_heap, (parts[index_min_value][0], index_min_value))
        
    return sorted_list

def criar_entrada(n):
  random_values = np.random.randint(0, n, n-1)
  entrada = np.arange(n-1) + random_values
  return entrada.tolist()

import numpy as np
lista1 = criar_entrada(10000)

start_time = time.time()
result_quadratic = sqrt_sort_quadratic(lista1)
print(f"Tempo utilizando Bubblesort: {time.time() - start_time}")

start_time = time.time()
result_heap = sqrt_sort_heap(lista1)
print(f"Tempo utilizando Heap: {time.time() - start_time}")
