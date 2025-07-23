import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation


def reconstruct_path(pred, target):
    path = []
    while target != -1:
        path.append(target)
        target = pred[target]

    path.reverse()

    return path


def draw_path(matrix, path, blink=False, bg_color="#1e1e2f", edge_color="#00CED1",
              node_color="#FFD700", arrowstyle='-|>', font_size=10):

    G = nx.DiGraph()
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        weight = matrix[u][v]
        G.add_edge(u, v, weight=weight)

    # Novo layout para visualização clara
    if len(path) <= 10:
        pos = nx.spring_layout(G, seed=42, k=1.5)
    elif len(path) <= 25:
        pos = nx.shell_layout(G)
    else:
        pos = {node: (i, 0) for i, node in enumerate(path)}  # Layout linear

    fig, ax = plt.subplots(figsize=(max(8, len(path)*0.5), 6))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    plt.axis('off')

    edge_labels = nx.get_edge_attributes(G, 'weight')

    def draw_frame(i):
        ax.clear()
        ax.set_facecolor(bg_color)
        current_node = path[i]
        next_node = path[i + 1] if i < len(path) - 1 else None

        edge_colors = []
        for (u, v) in G.edges():
            if u == current_node and v == next_node:
                edge_colors.append("red")
            else:
                edge_colors.append(edge_color)

        nx.draw_networkx_edges(G, pos, ax=ax, edge_color=edge_colors,
                               arrows=True, arrowstyle=arrowstyle, arrowsize=25, width=2)

        custom_edge_labels = {}
        for (u, v), label in edge_labels.items():
            if u == current_node and v == next_node:
                custom_edge_labels[(u, v)] = f"💰 {label}"
            else:
                custom_edge_labels[(u, v)] = str(label)

        nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=custom_edge_labels,
                                     font_color="white", font_size=font_size,
                                     bbox=dict(facecolor="black", edgecolor="none", pad=2))

        node_colors = []
        for node in G.nodes():
            if node == current_node:
                node_colors.append("red")
            else:
                node_colors.append(node_color)

        node_size = 700 if len(path) <= 20 else 500

        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                               node_size=node_size, edgecolors="black", linewidths=2)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=font_size + 2,
                                font_color="black", font_weight="bold")

    def draw_static():
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color=edge_color,
                               arrows=True, arrowstyle=arrowstyle, arrowsize=25, width=2)
        nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=edge_labels,
                                     font_color="white", font_size=font_size,
                                     bbox=dict(facecolor="black", edgecolor="none", pad=2))
        node_size = 700 if len(path) <= 20 else 500
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_color,
                               node_size=node_size, edgecolors="black", linewidths=2)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=font_size + 2,
                                font_color="black", font_weight="bold")

    if blink:
        ani = animation.FuncAnimation(fig, draw_frame,
                                      frames=len(path),
                                      interval=850,
                                      repeat=True)
    else:
        draw_static()

    plt.tight_layout()
    plt.show()