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
├── datasets/ # Graph data files
└── report.txt # Performance results and path outputs

## Requirements 

Python 3.8+
No external libraries required

## Implemented Features

- [x] **Graph Loader**: Reads `.txt` files and builds an adjacency matrix using `float('inf')` for missing edges.
- [x] **Dijkstra's Algorithm**: Finds the shortest paths from a source vertex to all others using the adjacency matrix representation.
- [x] **Bellman-Ford Algorithm**: Computes shortest paths from a single source and supports negative weights.
- [x] **Path Reconstruction**: Rebuilds the shortest path from the predecessor list returned by the algorithms.
- [ ] Performance measurement (time, cost, path)

---

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