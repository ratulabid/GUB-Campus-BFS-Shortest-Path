# GUB Campus Navigation & Shortest Path Finder Using BFS

A graph-based campus navigation system developed using **Python** and the **Breadth-First Search (BFS)** algorithm.

The project models Green University of Bangladesh (GUB) campus locations as an **undirected graph** and finds the shortest path between any two selected locations. It also maintains a **parent tracking dictionary** to reconstruct and display the exact ordered path from the starting location to the target.

> This project uses an academic graph model of campus locations for demonstrating BFS. It is not intended to represent an exact geographical map of the campus.

---

## 📌 Project Overview

Finding a path between two locations can be represented as a graph problem.

In this project:

- Each campus location is represented as a **vertex (node)**.
- A direct connection between two locations is represented as an **edge**.
- **BFS** is used to explore the graph level by level.
- A **parent dictionary** is maintained during BFS.
- The parent information is used to reconstruct the exact shortest path.
- The program calculates the total number of **edge steps** between the selected locations.

---

## 🎯 Objectives

The main objectives of this project are:

- Represent campus locations using a graph.
- Implement Breadth-First Search (BFS).
- Find the shortest path between two locations.
- Maintain parent information during BFS.
- Reconstruct the exact path using backtracking.
- Display the BFS traversal order.
- Calculate the total number of edge steps.
- Handle invalid and identical start/target locations.

---

## ✨ Features

- 🗺️ Graph-based campus representation
- 🔎 Breadth-First Search (BFS)
- 🧭 Shortest path detection
- 🌳 Parent tracking dictionary
- 🔄 Path reconstruction using backtracking
- 📋 BFS traversal order
- 📍 Available campus location list
- 🔤 Case-insensitive location input
- ⚠️ Invalid location handling
- 🎯 Same start and target handling
- 📊 Total edge-step calculation

---

## 🧠 Data Structures & Algorithms

### Graph

The campus is represented using an **undirected adjacency list**.

Example:

```python
"Main Gate": [
    "Security Checkpoint",
    "Transport & Parking Area"
]
