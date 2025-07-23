# shortest-path-algorithms

This project implements two shortest path algorithms, **Dijkstra** and **Bellman-Ford** using an **adjacency matrix** representation.  
It is based on a practical assignment for the *Graph Theory* course (CSI466) from Federal University of Ouro Preto(UFOP), with real-world datasets.

## Project Structure

shortest_path_algorithms/
├── main.py # Script to run tests and measure performance
├── graph_loader.py # Function to load graphs from .txt files
├── dijkstra.py # Dijkstra algorithm implementation
├── bellman_ford.py # Bellman-Ford algorithm implementation
├── utils.py # Utility functions
├── interface.py # Graphical interface for interactive visualization
├── datasets/ # Graph data files
├── report.py # Performance test generator
└── report.txt # Performance results and path outputs

## Requirements 

- Python 3.8+
- Libraries:
  - `tkinter`
  - `networkx`
  - `matplotlib`

Install with:

```bash
pip install matplotlib networkx

## Implemented Features

- [x] **Graph Loader**: Reads `.txt` files and builds an adjacency matrix using `float('inf')` for missing edges.
- [x] **Dijkstra's Algorithm**: Finds the shortest paths from a source vertex to all others using the adjacency matrix representation.
- [x] **Bellman-Ford Algorithm**: Computes shortest paths from a single source and supports negative weights.
- [x] **Path Reconstruction**: Rebuilds the shortest path from the predecessor list returned by the algorithms.
- [x] **Performance measurement (time, cost, path)**: Computes execution time, cost and full path, with timeout and memory-out handling.

---

🖥️ Graphical Interface
The interface.py file launches a modern, colorful and animated UI using Tkinter.

🎨 Features:
Dark mode layout with custom fonts and colors

Buttons with icons

Input of origin and target vertices

Result box with:

⏱️ Time

💰 Cost

🧭 Path

Animated drawing of the shortest path:

Arrows and weights shown

Vertices blinking during animation

Only the computed path is shown (not the full graph)

🔧 Usage
bash
Copiar
Editar
python interface.py


## 📥 How to use the Graph Loader function 

The `graph_loader.py` module contains a function to import graphs from `.txt` files into an adjacency matrix.

## 📈 How to use the Dijkstra algorithm

The `dijkstra.py` module implements Dijkstra's algorithm to compute the shortest paths from a source vertex using an adjacency matrix.

### 🔧 Usage

dist, pred = dijkstra(matrix, origin)
matrix: adjacency matrix of the graph
origin: starting vertex index

## 🧮 How to use the Bellman-Ford algorithm

The `bellman_ford.py` module implements the optimized Bellman-Ford algorithm to find the shortest paths from a source vertex using an adjacency matrix.

### 🔧 Usage

dist, pred = bellman_ford(matrix, source)

## 🧩 How to reconstruct the shortest path

The `utils.py` module provides a helper function to rebuild the shortest path from the predecessor list returned by the algorithms.

### 🔧 Usage

from utils import reconstruct_path

path = reconstruct_path(pred, target)

---

## 📊 How to generate the report

The `report.py` script automates the evaluation of the shortest path algorithms, measuring runtime, cost, and path.

### 🔧 Usage

python report.py

🎯 How to draw the shortest path visually

from utils import draw_path
draw_path(matrix, path, blink=True)

📊 How to generate the performance report
The report.py script runs the shortest path algorithms over multiple files and vertex pairs.

🔧 Usage
python report.py

👩‍🎓 Authors
Developed by Laura Almeida Silveira - UFOP – CSI466 – 2025