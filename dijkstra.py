def dijkstra(matrix, origin):
    num_vertices = len(matrix)
    
    dist = [float('inf')] * num_vertices 
    pred = [-1] * num_vertices            
    dist[origin] = 0 

    Q = set(range(num_vertices))

    while Q:

        shortest_dist = float('inf')
        u = -1
        for v in Q:
            if dist[v] < shortest_dist:
                shortest_dist = dist[v]
                u = v

        Q.remove(u) 

        for v in range(num_vertices):
            w = matrix[u][v]
            if w != float('inf') and v in Q: 
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w         
                    pred[v] = u  

    return dist, pred