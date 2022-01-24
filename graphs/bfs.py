from queue import Queue
from vertex import Vertex as V


def bfs(v, adj, start_vertex):
    q = Queue()
    
    print(v[start_vertex])
    v[start_vertex].visited = True
    for u in adj[start_vertex]:
        q.push(u)
    
    while True:
        current = q.pop()
        if current == None:
            break
        if current.data.visited:
            continue
        else:
            print(current.data)
            current.data.visited = True
            neighbors = adj[current.data.num]
            for u in neighbors:
                q.push(u)

if __name__ == '__main__':
    # 8 vertices with the following values: 9, 2, 16, 5, 15, 10, 7, 11
    v = [V(0, 9), V(1, 2), V(2, 16), V(3, 5), V(4, 15), V(5, 10), V(6, 7), V(7, 11)]
    adj = [
        # 1st vertex
        [v[1], v[3], v[6]],
        # 2nd vertex
        [v[0], v[2]],
        # 3rd vertex
        [v[1], v[5]],
        # 4th vertex
        [v[0], v[4]],
        # 5th vertex
        [v[3], v[5]],
        # 6th vertex
        [v[2], v[4], v[7]],
        # 7th vertex
        [v[0], v[7]],
        # 8th vertex
        [v[6], v[5]]
    ]

    bfs(v, adj, 0)
