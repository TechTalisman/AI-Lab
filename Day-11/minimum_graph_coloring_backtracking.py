# This program finds the minimum number of colors required to color a graph using Backtracking so that no adjacent vertices share the same color.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['D', 'E', 'G'],
    'G': ['E', 'F']
}

def is_safe(vertex, color, colors, graph):
    for neighbor in graph[vertex]:
        if colors.get(neighbor) == color:
            return False
    return True


def graph_coloring_util(vertices, graph, m, colors, index):
    if index == len(vertices):
        return True

    vertex = vertices[index]

    for color in range(1, m + 1):
        if is_safe(vertex, color, colors, graph):
            colors[vertex] = color

            if graph_coloring_util(vertices, graph, m, colors, index + 1):
                return True

            colors[vertex] = 0

    return False


def find_minimum_colors(graph):
    vertices = list(graph.keys())
    n = len(vertices)

    for m in range(1, n + 1):
        colors = {v: 0 for v in vertices}

        if graph_coloring_util(vertices, graph, m, colors, 0):
            print(f"\nColoring Possible with {m} colors")
            for vertex in vertices:
                print(f"Vertex {vertex} → Color {colors[vertex]}")
            print(f"\nMinimum number of colors required = {m}")
            return 

find_minimum_colors(graph)
