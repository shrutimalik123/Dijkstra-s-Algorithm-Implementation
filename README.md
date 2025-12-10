# Dijkstra's Algorithm Implementation

DSA Focus: Graphs, Priority Queues (Heaps)

## Description
This project implements Dijkstra's Algorithm in Python to find the shortest path between nodes in a weighted graph. It uses a dictionary to represent the graph and a priority queue (via `heapq`) for efficient node selection.

## Features
- **Graph Representation**: Uses an adjacency dictionary.
- **Priority Queue**: Uses a min-heap to efficiently select the next closest node.
- **Path Reconstruction**: logic to backtrack and find the exact path taken.

## Usage
Run the script to see the algorithm in action on a sample graph of cities.

```bash
python dijkstra.py
```

## Sample Output
```text
Finding shortest path from New York to Columbus...
Shortest Distance: 585
Path: New York -> Philadelphia -> Pittsburgh -> Columbus
```
