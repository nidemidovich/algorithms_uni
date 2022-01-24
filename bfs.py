from queue import Queue
from vertex import Vertex as V

# 8 vertices with the following values: 9, 2, 16, 5, 15, 10, 7, 11
v = [V(0, 9), V(1, 2), V(2, 16), V(3, 5), V(4, 15), V(5, 10), V(6, 7), V(7, 11)]
adj = [
    # 1st vertex
    [v[1], v[2], v[3]],
    # 2nd vertex
    [v[0], v[2], v[4], v[5]],
    # 3rd vertex
    [v[0], v[1], v[3], v[5]],
    # 4th vertex
    [v[0], v[2], v[7]],
    # 5th vertex
    [v[1], v[5]],
    # 6th vertex
    [v[1], v[2], v[4], v[6]],
    # 7th vertex
    [v[2], v[5], v[7]],
    # 8th vertex
    [v[3], v[7]]
]

def bfs(adj, start_vertex):
    q = Queue()
    
    print(v[start_vertex])
    v[start_vertex].visited = True
    for u in adj[start_vertex]:
        q.push(u)
    
    while (q.size > 0):
        current = q.pop()
        if current.data.visited:
            continue
        else:
            print(current.data)
            current.data.visited = True
            neighbors = adj[current.data.num]
            for u in neighbors:
                q.push(u)

bfs(adj, 0)