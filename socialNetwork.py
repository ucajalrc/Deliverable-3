"""
This file contains the main implementation for the SocialNetwork class.
It provides an optimized in-memory graph structure for simulating and analyzing
a social network. Users can be added, connected, profiled, ranked by influence,
and traversed using BFS. Caching and efficient data structures ensure scalability
for large networks.
"""

from collections import defaultdict, deque
import heapq

class SocialNetwork:
    """
    Social network graph optimized for performance and scaling.
    Uses defaultdict for efficient adjacency lists and caching for analytics.
    Scales well to large datasets.
    """

    def __init__(self):
        self.adj = defaultdict(set)    # User connections (adjacency list)
        self.profiles = {}             # User profiles (hash table)
        self._centrality_cache = None  # Cache for degree centrality

    def add_user(self, user_id):
        """Add a user to the network."""
        self.adj[user_id]
        self.profiles.setdefault(user_id, {})

    def add_connection(self, user_from, user_to):
        """Add a directed connection from user_from to user_to."""
        self.adj[user_from].add(user_to)
        self._centrality_cache = None

    def add_profile(self, user_id, profile_dict):
        """Update or create a profile for the user."""
        self.profiles.setdefault(user_id, {}).update(profile_dict)

    def get_profile(self, user_id):
        """Get the profile dictionary for a user, or None."""
        return self.profiles.get(user_id, None)

    def degree_centrality(self):
        """Calculate or return cached degree centrality for all users."""
        if self._centrality_cache is None:
            self._centrality_cache = {user: len(neigh) for user, neigh in self.adj.items()}
        return self._centrality_cache

    def top_k_influencers(self, centrality, k):
        """Find k users with highest degree (most connections)."""
        return heapq.nlargest(k, centrality.items(), key=lambda x: x[1])

    def bfs(self, start_user):
        """Breadth-first search to find all reachable users."""
        if start_user not in self.adj:
            return set()
        visited = set([start_user])
        queue = deque([start_user])
        while queue:
            user = queue.popleft()
            for neighbor in self.adj[user]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

# Example usage/demo (uncomment to try):
# def main():
#     print("Demo: Creating a mini social network.")
#     network = SocialNetwork()
#     network.add_user("alice")
#     network.add_user("bob")
#     network.add_connection("alice", "bob")
#     network.add_profile("alice", {"bio": "Test user"})
#     print("Profile for 'alice':", network.get_profile("alice"))
#     print("Degree centrality (connections per user):", network.degree_centrality())
#     print("All users reachable from 'alice':", network.bfs("alice"))
#
# if __name__ == "__main__":
#     main()
