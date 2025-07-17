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

- [x] **Graph Loader**: Reads `.txt` files and builds an adjacency matrix using `float('inf')` for missing edges
- [ ] Dijkstra's Algorithm
- [ ] Bellman-Ford Algorithm
- [ ] Path reconstruction
- [ ] Performance measurement (time, cost, path)

---

## 📥 How to use the Graph Loader function 

The `graph_loader.py` module contains a function to import graphs from `.txt` files into an adjacency matrix.

