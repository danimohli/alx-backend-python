#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient's org method.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, og, mock_json):
        """
        Test that GithubOrgClient.org calls get_json with the correct URL.
        """
        mock_json.return_value = {"login": og}
        client = GithubOrgClient(og)
        result = client.org
        mock_json.assert_called_once_with(f"https://api.github.com/orgs/{og}")

        self.assertEqual(result, {"login": og})


if __name__ == "__main__":
    unittest.main()
