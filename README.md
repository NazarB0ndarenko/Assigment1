# Artificial Intelligence Assignment 1  

---

## 1. Overview

This project implements and compares two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The goal of the assignment is to evaluate how different uninformed search strategies behave when solving the same search problem on multiple datasets.

Each algorithm attempts to find a path between a start node and a goal node in a graph.

---

## 2. Technologies Used

- Python 3.10
- NetworkX (for graph generation)
- Standard Python libraries (time, collections)

---

## 3. Files responsibilities 

- `generator.py` – Generates three different graph datasets
- `bfs.py` – Implements Breadth-First Search
- `dfs.py` – Implements Depth-First Search
- `main.py` – Executes experiments and prints comparative results

The algorithms are implemented manually and do not use built-in NetworkX search functions.

---

## 4. Search Algorithms

### 4.1 Breadth-First Search (BFS)

BFS explores nodes level by level using a queue

Properties:
- Complete (if solution exists, it will find it)
- Optimal in unweighted graphs (finds shortest path in terms of edges)
- Higher memory usage compared to DFS

Time Complexity: O(V + E)  
Space Complexity: O(V)

---

### 4.2 Depth-First Search (DFS)

DFS explores as deep as possible before backtracking using a stack.

Properties:
- May find a solution faster in some cases
- Does not guarantee shortest path
- Lower memory usage compared to BFS

Time Complexity: O(V + E)  
Space Complexity: O(V)

---

## 5. Experimental Setup

Three different graph datasets were generated random graph model:

1. Sparse graph (low edge probability)
2. Medium-density graph
3. Dense graph (high edge probability)

Each graph:
- Contains 25 nodes
- Uses the same start and goal nodes for both algorithms

Metrics collected:

- Number of visited nodes
- Path length
- Execution time
- Resulting path

---

## 6. Comparative Analysis

### Observed Behavior

Across multiple runs, the following patterns were observed:

- BFS consistently finds the shortest path in unweighted graphs.
- DFS sometimes finds longer paths due to its depth-first nature.
- BFS typically visits more nodes in deeper or sparse graphs.
- DFS may explore fewer nodes but can produce non-optimal solutions.
- In dense graphs, performance differences between BFS and DFS decrease because the graph diameter tends to be smaller.

### Performance Trends

| Property        | BFS | DFS |
|----------------|-----|-----|
| Optimal Path   | Yes | No |
| Memory Usage   | Higher | Lower |
| Deterministic Shortest Path | Yes | No |
| Risk of Deep Exploration | No | Yes |

---

## 7. Conclusion

Breadth-First Search is optimal and guarantees the shortest path in unweighted graphs, but at the cost of increased memory consumption and potentially exploring more nodes.

Depth-First Search may reach the goal faster in some cases and often uses less memory, but it does not guarantee an optimal solution and may explore long irrelevant paths.

The choice between BFS and DFS depends on:

- Whether optimality is required
- Memory constraints
- Graph structure (sparse vs dense)
- Expected depth of the solution

In summary:

- If shortest path is required → BFS is preferred.
- If memory is limited or solution depth is small → DFS may be acceptable.
