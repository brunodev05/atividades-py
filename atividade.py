def merge_sort(arr):
    steps = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        steps += merge_sort(left_half)
        steps += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            steps += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            steps += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            steps += 1

    return steps

if __name__ == "__main__":
    import random

    # Gere uma lista de 10 nomes aleatórios
    nomes = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack"]
    random.shuffle(nomes)

    print("Lista não ordenada:", nomes)

    # Ordenar a lista usando o Merge Sort
    passos = merge_sort(nomes.copy())

    print("\nLista ordenada:", nomes)
    print("\nQuantidade de passos efetuados:", passos)
