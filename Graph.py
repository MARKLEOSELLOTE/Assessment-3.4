from collections import deque

LABELS = {1: "S", 2: "E", 3: "L", 4: "L", 5: "O", 6: "T", 7: "E"}

GRAPH = {
    1: [2, 5, 3],
    2: [1, 4, 6],
    3: [1, 5, 6],
    4: [2, 7],
    5: [1, 3, 7],
    6: [3, 2],
    7: [4, 5],
}


def show(order):
    return " - ".join(LABELS[n] for n in order)


def graph_bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
        for nb in graph[v]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return result


def graph_dfs(graph, v, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(v)
    result.append(v)
    for nb in graph[v]:
        if nb not in visited:
            graph_dfs(graph, nb, visited, result)
    return result


if __name__ == "__main__":
    print("BFS:", show(graph_bfs(GRAPH, 1)))
    input("Enter to see DFS")
    print("DFS:", show(graph_dfs(GRAPH, 1)))