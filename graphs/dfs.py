from stack import StackClassic
from vertex import Vertex as V


def dfs(v, adj, start_vertex):
    s = StackClassic()

    current = v[start_vertex]
    print(current)
    current.visited = True
    s.push(adj[start_vertex][0])

    while True:
        current = s.view()
        if current == None:
            break
        if current.visited != True:
            print(current)
            current.visited = True
            for u in adj[current.num]:
                flag = True
                if u.visited != True and flag == True:
                    s.push(u)
                    flag = False
        else:
            s.pop()


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

    dfs(v, adj, 0)
    