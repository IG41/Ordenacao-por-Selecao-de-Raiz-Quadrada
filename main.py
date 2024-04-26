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
    parts = [sorted(array[i:i+sqrt_n]) for i in range(0, len(array), sqrt_n)]
    
    heap = [(part[0], i, 0) for i, part in enumerate(parts) if part]
    heapq.heapify(heap)
    
    aux_vector = []

    while heap:
        min_val, part_index, idx = heapq.heappop(heap)
        aux_vector.append(min_val)

        if idx + 1 < len(parts[part_index]):
            next_val = parts[part_index][idx + 1]
            heapq.heappush(heap, (next_val, part_index, idx + 1))
    return aux_vector

def criar_entrada(n):
  random_values = np.random.randint(0, n, n-1)
  entrada = np.arange(n-1) + random_values
  return entrada.tolist()
import numpy as np
lista1 = criar_entrada(10000001)


array = [8, 11, 6, 4, 12, 7, 5, 15, 17, 1, 2]
print("Array original:", array)
# print("Tempo: ", inicio - time.time())

start_time = time.time()
result_quadratic = sqrt_sort_quadratic(lista1)
# print("\nResultado final usando método quadrático:", result_quadratic)
# print(f"Tamanho: {len(result_quadratic)}")
print(f"Tempo: {time.time() - start_time}")

start_time = time.time()
result_heap = sqrt_sort_heap(lista1)
#print("\nResultado final usando heap:", result_heap)
print(f"Tempo: {time.time() - start_time}")
