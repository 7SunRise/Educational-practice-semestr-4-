class SortingAlgorithms:



    # Сортировка заключается в том, что мы изначально сравниваем элементы, которые находятся
    # на некотором расстоянии друг от друга. Если были изменения, то мы повторяем сортировку
    # с этим же расстоянием. Если изменений не было, то уменьшаем расстояние и повторяем.
    # Работа заканчивается, когда не было произведено изменений с шагом 1.
    def CombSort(result): # Сортировка прочесыванием. На вход подается массив.
        length = len(result)
        for step in range(length - 1, 0, -1):
            while True:
                changes = 0
                for i in range(0, length):
                    if ((i + step) > length - 1):
                        break
                    else:
                        if (result[i] > result[i + step]):
                            result[i], result[i + step] = result[i + step], result[i]
                            changes += 1
                if changes == 0:
                    break
        return result



    # Сортировка заключается в последовательном считывании элементов из массива. Считанный
    # элемент "вставляется" в подходящее место среди уже отсортированных элементов.
    def insertion_sort(array): # Сортировка вставками. На вход подается массив.
        for i in range(1,len(array)):
            x = array[i]
            j = i
            while j > 0 and array[j - 1] > x:
                array[j] = array[j -1]
                j -= 1
            array[j] = x
        return array



    # Сортировка заключается в том, что мы проходим по всему не отсортированному массиву и ищем
    # в нем минимальное значение. Далее меняем минимальную по значению позицию с первой
    # не отсортированной позицией. Повторяем действия, исключив отсортированную часть.
    def selection_sort(array): # Сортировка выбором. На вход подается массив.
        for i in range(0, len(array) - 1):
            minimal = i
            for k in range(i + 1, len(array)):
                if array[k] < array[minimal]:
                    minimal = k
            array[i], array[minimal] = array[minimal], array[i]
        return array



    # Сортировка заключается в том, что мы составляем подсписки из начального массива, которые
    # находятся на определенном расстояние (удобно брать половину массива). Далее сортировка
    # повторяетя, но уже с меньшим расстоянием. Продолжается до тех пор, пока расстояние
    # не станет равным 1.
    def shell_sort(array): # Сортировка Шелла. На вход подается массив.
        last_index = len(array)
        step = len(array) // 2
        while step > 0:
            for i in range(step, last_index):
                j = i
                delta = j - step
                while delta >=0 and array[delta] > array[j]:
                    array[delta], array[j] = array[j], array[delta]
                    j = delta
                    delta = j - step
            step -= 1
        return array



    # Сортировка заключается в том, что сначала мы сортируем элементы по старшему разряду.
    # Далее мы уменьшаем порядок разряда на 1 и сортируем повторно. Продолжается до тех пор,
    # пока массив не будет отсортирован по разряду единиц.
    def radix_sort(array): # Поразрядная сортировка. На вход подается массив.
        length = len(str(max(array)))
        for i in range(length):
            B = [[] for k in range(10)]
            for x in array:
                figure = x // 10**i % 10
                B[figure].append(x)
            array = []
            for k in range(10):
                array = array + B[k]
        return array



    # Сортировка заключается в том, что мы создаем сортирующее дерево, в котором меняем первый
    # и последний элемент местами. После замены сортируем заново и меняем уже n-1 элемент с 1.
    # Процесс заканчивается, когда мы сортируем дерево из нуля элементов.
    def heap_sort(arr): # Пирамидальная сортировка. На вход подается массив.
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i: # если все верно
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        n = len(arr)
        for i in range(n // 2, -1, -1):
            heapify(arr, n ,i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr



    # Сортировка заключается в том, что мы разбиваем массив по одному элементу, а далее
    # сравниваем "попарно" и обьединяем. Повторяем процесс до тех пор, пока мы
    # не соединим пары до длины изначального массива.
    def merge_sort(arr): # Сортировка слиянием. На вход подается массив. 
        if len(arr) == 1 or len(arr) ==  0:
            return arr
        L = merge_sort(arr[:len(arr) // 2])
        R = merge_sort(arr[len(arr) // 2:])
        n = m = k = 0
        C = [0] * len(arr)
        while n < len(L) and m < len(R):
            if L[n] <= R[m]:
                C[k] = L[n]
                n += 1
            else:
                C[k] = R[m]
                m += 1
            k += 1
        while n < len(L):
            C[k] = L[n]
            n += 1
            k += 1
        while m < len(R):
            C[k] = R[m]
            m += 1
            k += 1
        arr = C
        return arr



    # Сортировка заключается в том, что мы выбираем элемент из массива, относительно которого
    # сравниваем остальные. Те, что меньше, ставим левее выбранного элемента. Те, что больше,
    # правее выбранного элемента. Повторяем этот процесс для левой и правой стороны. Работа
    # заканчивается, когда будет отсортирована правая часть первого разбиения.
    def quick_sort(array, low, high): # Быстрая сортировка. На вход подается массив, 0  и len - 1
        def partition(array, low, high):
            pivot = array[high]
            i = low
            for j in range(low, high):
                if array[j] <= pivot:
                    array[i], array[j] = array[j], array[i]
                    i = i + 1
            array[i], array[high] = array[high], array[i]
            return i
        if low < high:
            pi = partition(array, low, high)
            quick_sort(array, low, pi - 1)
            quick_sort(array, pi + 1, high)
        return array
