class SearchAlgorithms:



    class Edge: # класс, использующийся в функции нахождения минимального покрывающего дерева
        def __init__(self, a, b, val):
            self.__start = a
            self.__end = b
            self.__weight = val

        @property
        def start(self):
            return self.__start

        @start.setter
        def start(self, val):
            self.__start = val

        @property
        def end(self):
            return self.__end

        @end.setter
        def end(self, val):
            self.__end = val

        @property
        def weight(self):
            return self.__weight

        @weight.setter
        def weight(self, val):
            self.__weight = val

        def __eq__(self, other):
            return (self.start == other.start and self.end == other.end) or (self.start == other.end and self.end == other.start)



    # Суть поиска в ширину - добавлять в конец очереди те элементы, в которые мы можем попасть из нынешнего, затем идти по очереди сначала, удаляя пройденные элементы.
    # Также мы должны помнить, в какие элементы уже ходили, и какие элементы уже в очереди, чтобы не дублироваться.
    def short_path(graph, startnode):          # Кратчайшие пути с помощью поиска в ширину. На вход подается
        def not_in(elem, ls):                  # массив строк таблицы смежности и индекс вершины, от которой              
            for i in range(0, len(ls)):        # ищут нужные пути. На выходе получаем двумерный массив, в котором
                if ls[i][0] == elem:           # visited[i][0] - индекс вершины, до которой искали путь, а visited[i][1] - сам путь
                    return False
            return True
        for i in range(0, len(graph)):
        graph[i] = [int(j) for j in graph[i]]
        queue, visited = [[startnode, 0]], []
        node = 0
        while queue:
            node = queue[0]
            queue.pop(0)
            for j in range(0, len(graph[node[0]])):
                if graph[node[0]][j] and not_in(j, visited) and not_in(j, queue):
                    queue.append([j, node[1]+1])
                    visited.append([j, node[1]+1])
        return visited



    # Суть заключается в том, что мы берем проивзольную вершину и методом в ширину проходимся по компоненте, которая содержит эту вершину.
    # Алгоритм завершается, когда все вершины будут рассмотрены.
    def amount_and_composition_of_connected_components_with_bfs(graph): # Количество и состав компонент связности с помощью поиска в ширину.
        for i in range(0, len(graph)):                                  # На вход подается массив строк таблицы смежности. На выходе получаем
            graph[i] = [int(j) for j in graph[i]]                       # двумерный массив, состоящий из компонент связности
        answer = []
        queue, visited, component = [], [], []
        i = 1
        for startnode in range(0, len(graph)):
            if startnode not in visited:
                queue.append(startnode)
            while queue:
                node = queue[0]
                visited.append(node)
                component.append(node)
                queue.pop(0)
                for j in range(0, len(graph[node])):
                    if graph[node][j] and j not in visited and j not in queue:
                        queue.append(j)
            if component:
                answer.append(component)
                component.clear()
                i += 1
        return answer



    # Суть заключается в том, что мы берем произвольную вершину и методом в глубину проходимся по компоненте, которая содержит эту вершину.
    # Алгоритм завершается, когда все вершины будут рассмотрены.
    def amount_and_composition_of_connected_components_with_dfs(graph): # Количество и состав компонент связности с помощью поиска в глубину.
        def depth(node, visited, graph):                                # На вход подается массив строк таблицы смежности. На выходе получаем
            visited.append(node)                                        # двумерный массив, состоящий из компонент связности
            for i in range(0, len(graph[node])):
                if graph[node][i] and i not in visited:
                    depth(i, visited, graph)
                else:
                    component.append(node)
        answer = []
        for i in range(0, len(graph)):
            graph[i] = [int(j) for j in graph[i]]
        visited = []
        i = 1
        component = []
        for startnode in range(0, len(graph)):
            if startnode not in visited:
                component.clear()
                depth(startnode, visited, graph)
                answer.append(component)
                i += 1
        return answer



    # Суть заключается в том, чтобы добавлять ребра в порядке возрастания их весов, которые бы не образовывали циклы в нашем графе.
    # Алгоритм завершается, когда будут соединены все вершины.
    def find_minimum_spanning_tree(graph):              # Алгоритм Крускала для нахождения минимального покрывающего дерева. На вход подается массив строк таблицы
        answer = []                                     # смежности. На выходе получаем двумерный массив, первый элемент которого представляет собой минимальную
        def dfs(node, visited, parent, subgraph):       # длину покрывающего дерева, а все остальные элементы это ребра-массивы, в которых первый два элемента индексы
            visited.append(node)                        # вершин, а последний длина данного ребра.
            for i in range(0, len(subgraph[node])):
                if subgraph[node][i]:
                    if i not in visited:
                        if dfs(i, visited, node, subgraph):
                            return True
                    elif parent != i:
                        return True
            return False
        def cycles(shortest, total_nodes, nodes):
            visited = []
            to_visit = list(nodes)
            last = shortest[-1]
            if last.start not in to_visit:
                to_visit.append(last.start)
            if last.end not in to_visit:
                to_visit.append(last.end)
            subgraph = [[] for i in range(0, total_nodes)]
            for i in range(0, total_nodes):
                subgraph[i] = [0 for i in range(0, total_nodes)]
            for i in range(0, len(shortest)):
                cur = shortest[i]
                subgraph[cur.start][cur.end] = cur.weight
                subgraph[cur.end][cur.start] = cur.weight
            for i in range(0, len(to_visit)):
                node = to_visit[i]
                if node not in visited:
                    if dfs(node, visited, -1, subgraph):
                        return True
            return False
            for i in range(0, len(graph)):
                graph[i] = [int(j) for j in graph[i]]
            total_nodes = len(graph)
            edges = []
            for i in range(0, total_nodes):
                for j in range(0, total_nodes):
                    path = graph[i][j]
                    if i != j and path:
                        temp = Edge(i, j, path)
                        if temp not in edges:
                            edges.append(temp)
            edges = sorted(edges, key=lambda item: item.weight)
            shortest, nodes, i, smallest_weight = [], [], 0, 0
            while len(nodes) < total_nodes:
                cur_edge = edges[i]
                shortest.append(cur_edge)
                if cycles(shortest, total_nodes, nodes):
                    shortest.remove(cur_edge)
                else:
                    if cur_edge.start not in nodes:
                        nodes.append(cur_edge.start)
                    if cur_edge.end not in nodes:
                        nodes.append(cur_edge.end)
                    smallest_weight += cur_edge.weight
                i += 1
    answer.append(smallest_weight)
    for i in range(0, len(shortest)):
        answer.append([{shortest[i].start}, {shortest[i].end}, {shortest[i].weight}])
    return answer



    # Суть заключается в том, что мы проходим по всем ребрам из стартовой вершины и присваиваем вершинам, в которые ведут эти ребра, временные
    # значения кратчайшего пути. Исключаем вершину, у которой рассмотрели все ребра. Делаем аналогичные действия с одной из вершиной, в которую
    # вело ребро. Алгоритм заканчивается, когда все вршины будут исключены из графа.
    def short_path_Deikstra(graph, start):              # Кратчайшие пути с помощью алгоритма Дейкстры. На вход подается массив строк таблицы
        answer = []                                     # смежности и вершина, от которой ищем расстояния. На выходе получаем двумерный массив, где
        for i in range(0, len(graph)):                  # элементами являются массивы, в которых первый элемент - стартовая вершина; второй 
            graph[i] = [int(j) for j in graph[i]]       # элемент - вершина, до которой ищем путь. Третий элемент - длина пути
        total_nodes = len(graph)
        queue = {}
        for i in range(0, total_nodes):
            if i == start:
                queue[i] = 0
            else:
                queue[i] = 99999999999
        while len(queue) > 0:
            closest = min(queue.items(), key=lambda x: x[1])  
            node, mark = closest[0], closest[1]
            for i in range(0, total_nodes):
                path = graph[node][i]
                if path and (i in queue.keys()):
                    if mark + path < queue[i]:
                        queue[i] = mark + path
            if start != node:
                answer.append([{start},{node},{mark}])
            queue.pop(node)
        return answer



    # Суть заключается в том, что мы постепенно увеличиваем максимальную длину пути от начльной вершины. Т.е. в начале рассматриваем пути из одного ребра,
    # далее из двух и т.д. Таким образом, вершинам будут придаваться временные кратчайшие пути. Алгоритм заканчивается, когда рассматриваются пути
    # длины n - 1, где n - число вершин.
    def short_path_Bellman_Ford(graph, start):      # Кратчайшие пути с помощью алгоритма Белламана-Форда. На вход поадется массив строк таблицы
        answer = []                                 # смежности и вершина, от которой ищем расстояния. На выходе получаем двумерный массив, где
        for i in range(0, len(graph)):              # элементами являются массивы, в которых первый элемент - стартовая вершина;
            graph[i] = [int(j) for j in graph[i]]   # второй элемент - вершина, до которой ищем путь. Третий элемент - длина пути.
        v = len(graph[i])
        distance = []
        for i in range(0, v):
            if i == start:
                distance.append(0)
            else:
                distance.append(float('inf'))
        for x in range(0, v-1):
            for i in range(0, v):
                for j in range(0, v):
                    path = graph[i][j]
                    if path != 0:
                        if distance[j] > distance[i] + path:
                            distance[j] = distance[i] + path
        for i in range(0, v):
            if i != start:
                answer.append([{start}, {i}, {distance[i]}])
        return answer



    # Суть заключается в том, что мы используем алгоритм Флери. Если из вершины выходит всего одно ребро, то мы переходим по нему и удаляем из списка, чтобы
    # не пройти по нему в будущем. Если ребер несколько, то выбираем то, которое при удалении не сделает вершину, в которую он ведет, недоступной.
    def find_eulerian_cycle_in_non_oriented(graph): # Нахождение Эйлерова цикла в неориентированном графе. На вход подается массив строк таблицы
        answer = []                                 # смежности. На выходе получаем либо 0, т.е. эйлерова цикла нет, либо двумерный массив, элементами которого являются
        def is_eulerian(graph, n):                  # массивы, первый и второй элементы которых это индексы вершин, а сам массив можно представить как ребро между ними.
            for i in range(n):
                path_count = 0
                for j in range(n):
                    if graph[i][j]:
                        path_count += 1
                if path_count % 2:
                    return False
            return True
        def dfs_count(node, visited, graph):
            reachable_vertices = 1
            visited.append(node)
            for i in range(0, len(graph[node])):
                if graph[node][i] and i not in visited:
                    reachable_vertices += dfs_count(i, visited, graph)
            return reachable_vertices
        def remove_path(begin, end, graph):
            graph[begin][end] = 0
            graph[end][begin] = 0
        def copy_2d_list(ls, n):
            copy = [list(ls[i]) for i in range(n)]
            return copy
        for i in range(len(graph)):
            graph[i] = [int(j) for j in graph[i]]
        n = len(graph)
        if is_eulerian(graph, n):
            print("В графе есть Эйлеров цикл:")
            node = 0
            while True:
                reachable_nodes = []
                for i in range(n):
                    if graph[node][i]:
                        reachable_nodes.append(i)
                count_paths = len(reachable_nodes)
                if not count_paths:
                    break
                elif count_paths == 1:
                    next_node = reachable_nodes[0]
                    remove_path(node, next_node, graph)
                    answer.append([node, next_node])
                    node = next_node
                else:
                    initial_node_count = dfs_count(node, [], graph)
                    for potential_path in reachable_nodes:
                        graph_copy = copy_2d_list(graph, n)
                        remove_path(node, potential_path, graph_copy)
                        if dfs_count(node, [], graph_copy) == initial_node_count:
                            remove_path(node, potential_path, graph)
                            answer.append([node, potential_path])
                            node = potential_path
                            break
            return answer
        else:
            return 0
