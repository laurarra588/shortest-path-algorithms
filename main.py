from graph_loader import load_graph
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from utils import reconstruct_path

if __name__ == "__main__":
    # Testing the shortest path from vertex 0 to 100 as requested
    origin = 0
    target = 100
    file_path = "datasets/facebook_combined.txt"

    try:
        matrix = load_graph(file_path)
    except Exception as error:
        print("Error loading graph:", error)
        exit()

    # Dijkstra
    dist_dijkstra, pred_dijkstra = dijkstra(matrix, origin)
    path_dijkstra = reconstruct_path(pred_dijkstra, target)

    # Bellman-Ford
    dist_bellman, pred_bellman = bellman_ford(matrix, origin)
    path_bellman = reconstruct_path(pred_bellman, target)

    print("Source vertex:", origin)
    print("Target vertex:", target)
    print()
    print("=== Dijkstra ===")
    print("Cost:", dist_dijkstra[target])
    print("Path:", path_dijkstra)
    print()
    print("=== Bellman-Ford ===")
    print("Cost:", dist_bellman[target])
    print("Path:", path_bellman)