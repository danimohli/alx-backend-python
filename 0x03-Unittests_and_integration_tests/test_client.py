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
    Test case for GithubOrgClient's methods.
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
        mock_get_json.assert_called_once_with(f"https://api.github.com/\
                                              orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})

    @patch('client.GithubOrgClient.org',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the expected URL.
        """
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/test_org/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
