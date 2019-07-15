
# we have implement an adjacency list which stores each node in a dictionary along with a set containing their adjacent nodes.
# As the graph is undirected each edge is stored in both incident nodes adjacent sets.

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# using stack data-structure to build-up and return a set of vertices that are accessible within the subjects connected component.

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# following will return {'D', 'B', 'F', 'C', 'E', 'A'} /
# {'A', 'C', 'D', 'F', 'E', 'B'} /
# {'C', 'B', 'A', 'F', 'E', 'D'} /
# {'D', 'C', 'A', 'E', 'F', 'B'} /
# {'D', 'B', 'A', 'C', 'F', 'E'} /
# {'C', 'E', 'B', 'D', 'F', 'A'}

#Random

print(dfs(graph, 'A'))


# iteratively solves the problem yielding each possible path when we locate the goal.

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Returns [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
print(list(dfs_paths(graph, 'A', 'F')) )


