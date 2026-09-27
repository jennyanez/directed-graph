# Directed Graph Creator

A desktop application for creating and exploring weighted directed graphs with Python, PyQt5, NetworkX and Matplotlib.

The application provides a graphical interface for editing graph nodes and edges, visualizing connections and running common graph traversal algorithms.

## Features

- Create, edit and delete nodes.
- Create, edit and delete weighted directed edges.
- Visualize the graph in a desktop GUI.
- Traverse the graph using:
  - Breadth-first search (BFS).
  - Depth-first search (DFS).
- Import and export graph data using a plain-text format.
- Work with self-loops and weighted connections.

## Tech stack

- Python
- PyQt5
- NetworkX
- Matplotlib
- NumPy
- Pandas

## Project structure

```text
.
├── requirements.txt
├── img/
└── src/
    ├── graph.py       # Graph data structure and graph operations
    ├── graph.txt      # Example graph data
    ├── interface.ui   # Qt Designer interface
    ├── main.py        # Application entry point
    └── window.py      # Main window and UI behavior
```

## Requirements

- Python 3
- pip
- A desktop environment supported by PyQt5

The exact package versions are pinned in [requirements.txt](requirements.txt).

## Installation

Clone the repository and install its dependencies:

```bash
git clone https://github.com/jennyanez/directed-graph.git
cd directed-graph
python -m venv .venv
```

Activate the virtual environment.

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application

The entry point is located in `src/main.py`:

```bash
python src/main.py
```

## Graph file format

The sample graph is stored in [src/graph.txt](src/graph.txt). Each edge is represented as:

```text
source; target; weight
```

For example:

```text
a; b; 8
b; c; 8
c; d; 6
```

Nodes can be declared separately using:

```text
Node: a
Node: b
```

Keep the spacing and separators consistent with the sample file when importing a graph.

## How to use it

1. Start the application with `python src/main.py`.
2. Create nodes and connect them with weighted directed edges.
3. Edit or delete graph elements from the interface as needed.
4. Run BFS or DFS to explore the graph.
5. Import an existing graph from a text file or export the current graph for later use.

## Project status

Educational desktop application for studying graph structures, weighted edges and traversal algorithms.
