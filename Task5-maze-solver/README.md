# Task 5 - Maze Solver (BFS)

A maze-solving program built as part of the Codmetric Internship Program, using the Breadth-First Search (BFS) algorithm to find the shortest path.

## Description
This project creates a program that solves a maze by finding the shortest path from a start point to an end point using the Breadth-First Search (BFS) algorithm. The maze is represented as a 2D grid, and the program explores all possible paths level by level to guarantee the shortest route is found.

## Features
- Maze represented as a 2D grid with clearly defined start and end points
- BFS algorithm implementation to traverse the maze and find the shortest path
- Displays the maze and highlights the solution path (text-based or simple graphics)
- Tested on multiple maze configurations to verify correctness

## Technologies Used
- Python

## How to Run
1. Clone this repository: git clone https://github.com/Kirubasri-RJ/Codmetric.git
2. Navigate to this folder: cd Codmetric/Task5-maze-solver-bfs
3. Run the program: python maze_solver.py
4. View the maze and the highlighted shortest path in the output

## How It Works
The BFS algorithm explores the maze level by level, starting from the entry point. It keeps track of visited cells to avoid revisiting them, and once the end point is reached, it traces back the path taken to display the shortest route from start to end.

## Future Improvements
- Add a graphical visualization of the maze-solving process
- Compare BFS performance with other algorithms (DFS, A*)
- Allow user to input custom maze configurations

## Author
Kirubasri RJ — Codmetric Internship Program
