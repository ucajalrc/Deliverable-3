"""
This file runs validation tests on edge cases for the SocialNetwork class.
It checks behavior for self-loops, duplicate connections, non-existent users,
and disconnected nodes. The output explains what each test is checking.
"""

from socialNetwork import SocialNetwork

def validation_tests():
    print("\nRunning validation tests for edge cases.")
    network = SocialNetwork()
    users = ["alice", "bob", "carol", "dave"]
    for user in users:
        network.add_user(user)

    # Test self-loop
    network.add_connection("alice", "alice")
    print("Added self-loop: alice -> alice")

    # Test duplicate connections
    network.add_connection("alice", "bob")
    network.add_connection("alice", "bob")
    print("Added duplicate connections: alice -> bob (should only store one)")

    # Test non-existent user in connection
    try:
        network.add_connection("eve", "alice")
        print("Tried adding connection with non-existent user 'eve' (should not crash).")
    except Exception as e:
        print("Error when adding connection with non-existent user:", e)

    # Test disconnected user
    network.add_user("eve")
    cent = network.degree_centrality()
    print("Degree centrality for all users (including 'eve'):", cent)

    # BFS from disconnected node
    bfs_eve = network.bfs("eve")
    print("BFS from 'eve' (should return only {'eve'}):", bfs_eve)

if __name__ == "__main__":
    validation_tests()
