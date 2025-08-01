# Social Network Analysis – Optimized Python Implementation

## Overview

This repository contains an optimized, scalable Python implementation of a social network analysis tool.  
It supports adding users and connections, storing and retrieving profiles, ranking users by influence, and efficient traversal of large networks.  
The code is modular and includes thorough unit tests, stress tests, validation checks, and performance benchmarking with charts.

## Setup Instructions

### 1. Clone the Repository
### 2. Set Up a Virtual Environment (Recommended)
``` bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
This project only needs matplotlib for plotting benchmark graphs (the rest is standard library):
``` bash
pip install matplotlib
```

## File Descriptions
1. socialNetwork.py
The main implementation of the SocialNetwork class (adding users, connections, profiles, ranking, BFS, and caching). Includes a commented-out demo in the main() function.

2. unitTest.py
Unit tests for all main features. Run to check correctness and edge cases.

3. stressTest.py
Script for stress-testing large networks (10,000+ users/connections). Measures analytics timing.

4. validationTest.py
Runs additional tests for edge cases like self-loops, duplicates, non-existent users, and disconnected nodes.

5. benchmark.py
Benchmarks analytics (centrality, influencer ranking, BFS) across network sizes. Plots a performance graph for scalability analysis.

6. report.docx
The project report with methodology, results, code/test snapshots, and detailed discussion.

## How to Run the Code
Activate your virtual environment:
``` bash
source venv/bin/activate    # Or venv\Scripts\activate on Windows
```

Run Unit Tests
``` bash
python unitTest.py
```
This will output test results for all major features.

Run Stress Test
```bash
python stressTest.py
```
Simulates a large network and prints timing results for analytics.

Run Validation Test
```bash
python validationTest.py
```
Checks for correct handling of special and edge cases.

Benchmark Performance and Plot Graphs
```bash
python benchmark.py
```
This generates a graph showing how analytics scale as your network size increases.
