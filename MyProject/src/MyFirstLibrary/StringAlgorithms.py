from random import uniform
class StringAlgorithms:



    # Суть заключается в том, что мы вводим состояние. Если следующий символ такой же, как и следующий в искомой подстроке,
    # то мы увеличиваем состояние на 1. Если нет, то ищем длину наибольшей строки, оканчивающейся на этот символ, у которой
    # прфеикс и суффикс одинаковые. Если состояние равно длине подстроки, то выводим индекс. Алгоритм заканчивается, если
    # пройден весь текст.
    def search_string_using_state_machine(file, pattern):       # Поиск подстроки с помощью конечного автомата. На вход подается считанный файл и
        answer = []                                             # искомая подстрока. На выходе получаем массив, который содержит все индексы
        def next_state(pattern, state, char, total_states):     # начала подстроки в нашем тексте. Если подстроки нет, то возварщается пустой массив.
            if state < total_states and pattern[state] == char:
                return state + 1
            for i in range(state, 0, -1):
                if pattern[i-1] == char and i % 2 == 0:
                    if pattern[:(i//2)] == pattern[(i//2):i]:
                        return i
            return 0
        def create_table(pattern, file, total_states):
            table = {}
            for i in file:
                if i not in list(table.keys()):
                    table[i] = [0 for j in range(total_states+1)]
            for state in range(total_states+1):
                for char in list(table.keys()):
                    table[char][state] = next_state(pattern, state, char, total_states)
            return table
        pattern = str(pattern)
        total_states = len(pattern)
        state = 0
        table = create_table(pattern, file, total_states)
        for i in range(len(file)):
            state = table[file[i]][state]
            if state == total_states:
                answer.append(i + 1 - total_states)
        return answer



    # Суть заключается в том, что используется префикс-функция. Если считанный из текста символ совпадает с символ из искомой подстроки,
    # то прибавляем 1 к значению префикс-функции. Если же не совпадает, то делаем сдвиг который зависит от префикс функции, чтобы
    # не потерять возможный индекс подстроки. Алгоритм заканчивается после протчения всего текста.
    def search_string_using_kmp(file, pattern):         # Поискл подстроки с помощью алгоритма Кнута-Морриса-Пратта. На вход подаеся
        def prefix(pattern):                            # считанный файл и искомая подстрока. На выходе получаем массив, который содержит
            chars = len(pattern)                        # все индексы начала подстроки в нашем тексте. Если подстроки нет, то возращается 0.
            prefix_array = [0 for i in range(chars)]
            prefix_value = 0
            for i in range(1, chars):
                if pattern[prefix_value] == pattern[i]:
                    prefix_value += 1
                    prefix_array[i] = prefix_value
                elif prefix_value != 0:
                    prefix_value = prefix_array[prefix_value - 1]
                else:
                    prefix_array[i] = 0
            return prefix_array
        def kmp(pattern, text):
            prefix_array = prefix(pattern)
            i, j = 0, 0
            found_pattern = []
            while (len(text) - i) >= (len(pattern) - j):
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                if j == len(pattern):
                    found_pattern.append(i - len(pattern))
                    j = prefix_array[j - 1]
                elif i < len(text) and pattern[j] != text[i]:
                    if j != 0:
                        j = prefix_array[j - 1]
                    else:
                        i += 1
            return found_pattern
        pattern = str(pattern)
        found_pattern = kmp(pattern, file)
        if found_pattern:
            for i in found_pattern:
                answer.append(i)
            return answer
        else:
            return 0



    # Суть заключается в том, что сравниваем искомую строку и текст с конца. Как только нашли несовпадение - сдвигаем искомую строку к символу,
    # где было несовпадение. При этом нужно чтобы теперь несовпавший символ совпал с последним входом этого символа в исходной строке.
    # Если такого символа в исходной строке нет, то всю строку перемещаем за этот символ. Алгоритм завершается после прочтения всего файла.
    def search_string_using_Boer_Mur(file, pattern):        # Поиск подстроки с помощью алгоритма Бойера-Мура. На вход подается файл и искомая подстрока.
        answer = []                                         # На выходе получаем массив, который содержит все индексы начала подстроки
        def bad_character(pattern):                         # в нашем тексте. Если подстроки нет, то возвращает 0.
            bad_character_array = [-1 for i in range(256)]  
            for i in range(len(pattern)):
                bad_character_array[ord(pattern[i])] = i
            return bad_character_array
        def bm_algo(pattern, text):
            bad_character_array = bad_character(pattern)
            found_pattern = []
            P, T = len(pattern), len(text)
            shift = 0
            while shift <= T - P:
                i = P - 1
                while i >= 0 and pattern[i] == text[shift+i]:
                    i -= 1
                if i < 0:
                    found_pattern.append(shift)
                    if shift + P < T:
                        shift += (P - bad_character_array[ord(text[shift+P])])
                    else:
                        shift += 1
                else:
                    shift += max(1, i - bad_character_array[ord(text[shift+i])])
            return found_pattern
        pattern = str(pattern)
        found_pattern = bm_algo(pattern, file)
        if found_pattern:
            for i in found_pattern:
                answer.append(i)
            return answer
        else:
            return 0



    # Суть заключается в том, что мы используем специальную хэщ-функцию, предложенную Рабином и Карпом. Вычисляем значение хэш-функции для нашей строки.
    # Далее сверяем значение хэша с хэшом части текста. Если совпадает, то нашли искомую подстроку. Если нет, то убираем из хэша первый
    # символ и добавляем следующий символ. Алгоритм заканчивается после прочтения всего файла.
    def search_string_using_Rabin_Karp(file, pattern):  # Поиск подстроки с помощью алгоритма Рабина-Карпа. На вход подается файл и искомая строка.
        answer = []                                     # На выходе получаем массив, который содержит все индексы начала подстроки
        def recalculate(old, text, i, b, p, l):         # в нашем тексте. Если подстроки нет, то возвращает 0.
            return ((old - (ord(text[i-l]) * b ** (l - 1)) % p) * b + ord(text[i])) % p
        def hash_func(pattern, base, prime, patlen):
            hash_value = 0 
            for i in range(patlen):
                hash_value += (ord(pattern[i]) * base ** (patlen - 1 - i))
            return hash_value % prime
        def rabin_karp(pattern, text):
            prime = 2 ** 61 - 1 
            base = int(uniform(0, prime - 1))  
            patlen, textlen = len(pattern), len(text)
            hash_pattern = hash_func(pattern, base, prime, patlen)
            hash_text = hash_func(text[:patlen], base, prime, patlen)
            found_pattern = []
            for i in range(patlen-1, textlen):
                if i >= patlen: 
                    hash_text = recalculate(hash_text, text, i, base, prime, patlen)
                if hash_text == hash_pattern:
                    j = 0
                    while j < patlen:
                        if pattern[j] != text[i - patlen + j + 1]:
                            break
                        j += 1
                    if j == patlen:
                        found_pattern.append(i - patlen + 1)
            return found_pattern
        pattern = str(pattern)
        found_pattern = rabin_karp(pattern, file)
        if found_pattern:
            for i in found_pattern:
                answer.append(i)
            return answer
        else:
            return 0
