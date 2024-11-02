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
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org calls get_json with the correct URL.
        """
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.git\
                                              hub.com/orgs/{org_name}")

        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()