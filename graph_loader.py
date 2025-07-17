def load_graph(filepath):

    with open(filepath, 'r') as file:
        lines = file.readlines()

    # First line has the number of vertices and edges
    num_vertices, num_edges = map(int, lines[0].strip().split())

    # Creates the matrix with infinity values
    matrix = []
    for i in range(num_vertices):
        row = [float('inf')] * num_vertices
        matrix.append(row)

    # Zeroing the diagonal
    for i in range(num_vertices):
        matrix[i][i] = 0

    # Go through each edge
    for i in range(1, len(lines)):
        line = lines[i]
        
        u, v, w = line.strip().split()
        u, v, w = int(u), int(v), float(w)
        matrix[u][v] = w

    return matrix