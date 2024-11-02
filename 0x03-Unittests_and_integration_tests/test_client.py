#!/usr/bin/env python3
"""
Unit test for the GithubOrgClient class in client.py.
"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for the GithubOrgClient class.
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org retrieves organization data correctly.

        - Uses patch to mock get_json.
        - Asserts get_json is called exactly once with the expected URL.
        """
        client = GithubOrgClient(org_name)
        client.org()

        expected_url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """
        Unit test for the _public_repos_url property of GithubOrgClient.

        - Uses patch to mock the org property and provide a fixed payload.
        - Asserts that _public_repos_url returns the repos_url
        from the payload.
        """
        payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient('test_org')
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Unit test for the public_repos method of GithubOrgClient.
        - Mocks get_json to return a predefined payload.
        - Mocks _public_repos_url to return a fixed URL.
        - Asserts that public_repos returns the correct list of repo names.
        - Verifies that get_json and _public_repos_url are called exactly
        once.
        """
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repos = ["repo1", "repo2", "repo3"]
        mock_get_json.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=unittest.mock.PropertyMock) as mock_repos_url:
            url_ = "https://api.github.com/orgs/test_org/repos"
            mock_repos_url.return_value = url_
            client = GithubOrgClient("test_org")

            result = client.public_repos()
            self.assertEqual(result, expected_repos)

            _json = "https://api.github.com/orgs/test_org/repos"
            mock_get_json.assert_called_once_with(_json)
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ("has_license_match", {"license": {"key": "mit"}}, "mit", True),
        ("no_license_match", {"license": {"key": "apache-2.0"}}, "mit", False),
        ("no_license_field", {}, "mit", False),
        ("license_key_missing", {"license": {}}, "mit", False)
    ])
    def test_has_license(self, _, repo_payload, license_key, expected):
        """
        Unit test for the has_license method of GithubOrgClient.
        - Parametrizes the test with different repository
        payloads and license keys.
        - Checks if has_license correctly identifies
        the presence of the specified license.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo_payload, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
        "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test suite for the GithubOrgClient.public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before any test cases run.
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if "orgs/" in url:
                return cls.org_payload
            elif "repos" in url:
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after all test cases have run.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that public_repos returns expected repo
        names based on fixture data.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that public_repos returns only repos with the Apache 2.0 license.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def setUpClass(cls):
        """
        Sets up resources for integration tests.
        Mocks requests.get to return example payloads for org and repos.
        """
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload
        ]

    def test_public_repos(self):
        """
        Test public_repos method to ensure it returns expected repos list.
        """
        client = GithubOrgClient("test_org")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos with a specific license filter ("apache-2.0").
        Ensures it returns only repos with the specified license.
        """
        client = GithubOrgClient("test_org")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """
        Stops the requests.get patcher after all tests have run.
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
