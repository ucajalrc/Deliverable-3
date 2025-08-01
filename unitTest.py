"""
This file contains unit tests for the SocialNetwork class.
Run this file to verify that all basic operations (user/connection/profile/bfs/analytics)
work correctly, including edge cases.
"""

import unittest
from socialNetwork import SocialNetwork

class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = SocialNetwork()
        self.network.add_user("alice")
        self.network.add_user("bob")
        self.network.add_connection("alice", "bob")
        self.network.add_profile("alice", {"bio": "CS major"})

    def test_add_user(self):
        self.network.add_user("carol")
        self.assertIn("carol", self.network.adj)

    def test_add_connection(self):
        self.network.add_user("carol")
        self.network.add_connection("bob", "carol")
        self.assertIn("carol", self.network.adj["bob"])

    def test_add_profile_and_get(self):
        self.network.add_profile("bob", {"bio": "Math major"})
        profile = self.network.get_profile("bob")
        self.assertEqual(profile["bio"], "Math major")

    def test_degree_centrality(self):
        cent = self.network.degree_centrality()
        self.assertEqual(cent["alice"], 1)
        self.assertEqual(cent["bob"], 0)

    def test_bfs(self):
        self.network.add_user("carol")
        self.network.add_connection("bob", "carol")
        reachable = self.network.bfs("alice")
        self.assertEqual(reachable, {"alice", "bob", "carol"})

    def test_top_k_influencers(self):
        cent = self.network.degree_centrality()
        top = self.network.top_k_influencers(cent, 1)
        self.assertEqual(top[0][0], "alice")  # Alice should have most connections

if __name__ == '__main__':
    print("Running unit tests for SocialNetwork implementation:")
    unittest.main()
