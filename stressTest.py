"""
This file stress-tests the SocialNetwork class with large numbers of users and connections.
It prints performance timings for analytics functions and BFS traversal.
Run this to see how the implementation handles large-scale networks.
"""

from socialNetwork import SocialNetwork
import random
import time

def stress_test(n_users=10000, n_connections=50000, top_k=10):
    print(f"\nStarting stress test with {n_users} users and {n_connections} connections.")
    network = SocialNetwork()
    # Add users
    for i in range(n_users):
        network.add_user(f"user_{i}")
    print("Finished adding users.")

    # Add connections
    for _ in range(n_connections):
        a, b = random.randint(0, n_users-1), random.randint(0, n_users-1)
        if a != b:
            network.add_connection(f"user_{a}", f"user_{b}")
    print("Finished adding connections.")

    # Centrality timing
    t0 = time.perf_counter()
    centrality = network.degree_centrality()
    t1 = time.perf_counter()
    print(f"Centrality computed in {t1 - t0:.2f} seconds.")

    # Top-K influencers timing
    t2 = time.perf_counter()
    top = network.top_k_influencers(centrality, top_k)
    t3 = time.perf_counter()
    print(f"Top-{top_k} influencers identified in {t3 - t2:.2f} seconds.")
    print("Top influencers (user, #connections):", top)

    # BFS timing
    t4 = time.perf_counter()
    start_user = f"user_{random.randint(0, n_users-1)}"
    reachable = network.bfs(start_user)
    t5 = time.perf_counter()
    print(f"BFS from {start_user} reached {len(reachable)} users in {t5 - t4:.2f} seconds.")

if __name__ == "__main__":
    stress_test()
