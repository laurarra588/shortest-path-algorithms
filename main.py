from graph_loader import load_graph
from dijkstra import dijkstra
from bellman_ford import bellman_ford

if __name__ == "__main__":
    # Testing the hortest path from vertex 0 to 100 as requested
    origin = 0
    target = 100
    file_path = "datasets/rg300_4730.txt"

    try:
        matrix = load_graph(file_path)
    except Exception as error:
        print("Error loading graph:", error)
        exit()

    dist, pred = dijkstra(matrix, origin)
    dist2 , pred2 = bellman_ford(matrix,0)

    print("origin:", origin)
    print("Target:", target)
    print("Cost using dijkstra:", dist[target])
    print("Cost using Bellman_ford:", dist2[100])