def quick_sort(arr, low, high):
    steps = 0

    if low < high:
        pivot_index, steps_partition = partition(arr, low, high)
        steps += steps_partition

        steps += quick_sort(arr, low, pivot_index)
        steps += quick_sort(arr, pivot_index + 1, high)

    return steps

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    steps = 0

    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
            steps += 1

        while arr[right] >= pivot and right >= left:
            right = right - 1
            steps += 1

        if right < left:
            done = True
        else:
            # Swap arr[left] and arr[right]
            arr[left], arr[right] = arr[right], arr[left]
            steps += 1

    # Swap arr[low] and arr[right]
    arr[low], arr[right] = arr[right], arr[low]
    steps += 1

    return right, steps

if __name__ == "__main__":
    import random

    # Gere uma lista de 10 nomes aleatórios
    nomes = random.sample(["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack"], 10)

    print("Lista não ordenada:", nomes)

    # Ordenar a lista usando o Quick Sort
    passos = quick_sort(nomes, 0, len(nomes) - 1)

    print("\nLista ordenada:", nomes)
    print("\nQuantidade de passos efetuados:", passos)
