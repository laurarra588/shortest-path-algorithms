from graph_loader import load_graph
from dijkstra import dijkstra

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

    print("origin:", origin)
    print("Target:", target)
    print("Cost:", dist[target])