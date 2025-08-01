"""
This script benchmarks and compares the performance of key SocialNetwork analytics
(centrality calculation, influencer ranking, and BFS) as the network scales.
It generates a performance graph and prints out what the graph means.
"""

from socialNetwork import SocialNetwork
import random
import time
import matplotlib.pyplot as plt

def benchmark_performance(user_sizes, connection_factor=5, top_k=10):
    setup_times, centrality_times, influencer_times, bfs_times = [], [], [], []
    for n_users in user_sizes:
        n_connections = n_users * connection_factor
        network = SocialNetwork()
        # Add users
        for i in range(n_users):
            network.add_user(f"user_{i}")
        # Add connections
        for _ in range(n_connections):
            a, b = random.randint(0, n_users-1), random.randint(0, n_users-1)
            if a != b:
                network.add_connection(f"user_{a}", f"user_{b}")
        # Analytics timing
        t0 = time.perf_counter()
        centrality = network.degree_centrality()
        t1 = time.perf_counter()
        top = network.top_k_influencers(centrality, top_k)
        t2 = time.perf_counter()
        start_user = f"user_{random.randint(0, n_users-1)}"
        reachable = network.bfs(start_user)
        t3 = time.perf_counter()
        centrality_times.append(t1-t0)
        influencer_times.append(t2-t1)
        bfs_times.append(t3-t2)
        print(f"\n--- Benchmark for {n_users} users ({n_connections} connections) ---")
        print(f"Centrality time: {t1-t0:.3f}s")
        print(f"Top-{top_k} influencer time: {t2-t1:.3f}s")
        print(f"BFS time from {start_user}: {t3-t2:.3f}s")

    plt.plot(user_sizes, centrality_times, label='Centrality Calculation')
    plt.plot(user_sizes, influencer_times, label='Top-K Influencers')
    plt.plot(user_sizes, bfs_times, label='BFS Traversal')
    plt.xlabel("Number of Users in Network")
    plt.ylabel("Time (seconds)")
    plt.title("Performance of SocialNetwork Analytics as Network Scales")
    plt.legend()
    plt.tight_layout()
    plt.show()
    print("\nGraph Interpretation: As the number of users in the social network grows, this plot shows how the time for each major analytic operation increases. Ideally, you want these lines to grow slowly, indicating good scalability. Sudden jumps might mean you are hitting algorithmic or memory bottlenecks.")

if __name__ == "__main__":
    # Example: test on 1K, 5K, 10K, 20K, 100k users
    benchmark_performance([1000, 5000, 10000, 20000, 100000])
