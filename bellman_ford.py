def bellman_ford(matrix, origin):
    num_vertices = len(matrix)
    
    dist = [float('inf')] * num_vertices
    pred = [-1] * num_vertices
    dist[origin] = 0

    for _ in range(num_vertices - 1):
        updated = False

        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = matrix[u][v]
                if weight != float('inf'):
                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        pred[v] = u
                        updated = True

        if not updated:
            break

    return dist, pred