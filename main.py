from graph_loader import load_graph

matrix = load_graph("./datasets/rg300_4730.txt")

print("Number of vertices:", len(matrix))
print("Weight of 0 → 1:", matrix[0][1])  # It must show 100
print("Weight of 0 → 59:", matrix[0][59])  # It must show 17