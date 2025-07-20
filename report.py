import time
from graph_loader import load_graph
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from utils import reconstruct_path

def algorithms(name, func, matrix, origin, target, timeout=1000):
    try:
        start_time = time.time()
        dist, pred = func(matrix, origin)
        elapsed = time.time() - start_time

        if elapsed > timeout:
            return f"{name}: TO"

        cost = dist[target]
        path = reconstruct_path(pred, target)

        if cost == float('inf') or not path:
            return f"{name}: no path"

        return f"{name}: time={elapsed:.4f}s, cost={cost}, path={path}"

    except MemoryError:
        return f"{name}: MO"
    except Exception as e:
        return f"{name}: error ({e})"

datasets = [
    "datasets/facebook_combined.txt",
    "datasets/rg300_4730.txt",
    "datasets/rome99c.txt",
    "datasets/toy.txt"
]

vertex_pairs = [
    (0, 100),
    (10, 50),
    (20, 80),
    (0, 1),
    (1, 299)
]

with open("report.txt", "w") as f:
    for dataset in datasets:
        f.write(f"===== FILE: {dataset} =====\n")
        print(f"===== FILE: {dataset} =====\n")

        try:
            matrix = load_graph(dataset)
        except MemoryError:
            f.write("Memory Out (MO)\n\n")
            print("Memory Out (MO)\n")
            continue
        except Exception as e:
            f.write(f"Error loading graph: {e}\n\n")
            print(f"Error loading graph: {e}\n")
            continue

        for origin, target in vertex_pairs:
            f.write(f"\nSource: {origin}, Target: {target} \n")
            print(f"\nSource: {origin}, Target: {target} ")

            res_dijkstra = algorithms("Dijkstra", dijkstra, matrix, origin, target)
            res_bellman = algorithms("Bellman-Ford", bellman_ford, matrix, origin, target)

            f.write(res_dijkstra + "\n")
            f.write(res_bellman + "\n")

            print(res_dijkstra)
            print(res_bellman)

        f.write("\n\n")