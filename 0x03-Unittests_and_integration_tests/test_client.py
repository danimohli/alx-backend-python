#!/usr/bin/env python3
"""
Module containing unit and integration tests for the GithubOrgClient class.
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for the GithubOrgClient class methods.
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that the org property retrieves organization
        data from the GitHub API.

        Verifies that `get_json` is called with the expected URL
        and is called exactly once.
        """
        client = GithubOrgClient(org_name)
        client.org()
        htpt = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(htpt)

    def test_public_repos_url(self):
        """
        Test the _public_repos_url property of GithubOrgClient.

        Ensures the `_public_repos_url` property returns
        the expected 'repos_url'
        from the organization's payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url":
                       "https://api.github.com/orgs/test_org/repos"}
            mock_org.return_value = payload
            client = GithubOrgClient('test_org')
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method to retrieve repository
        names from GitHub.

        Ensures that the `public_repos` method:
          - Calls the `get_json` method with the correct URL.
          - Returns the correct list of repository names
          based on the payload.
        """
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            _url = "https://api.github.com/orgs/test_org/repos"
            mock_url.return_value = _url
            client = GithubOrgClient('test_org')
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])

            mock_url.assert_called_once()
            _json = "https://api.github.com/orgs/test_org/repos"
            mock_get_json.assert_called_once_with(_json)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Unit test for the has_license method in GithubOrgClient.

        Confirms that has_license correctly identifies whether a given
        license key is associated with a repository.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test suite for GithubOrgClient using fixture data.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup resources for integration tests.
        Patches `requests.get` to return mock data
        for `org` and `repos_payload`
        to test GithubOrgClient without making real API calls.
        """
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload, cls.org_payload,
            cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Integration test for the public_repos method of GithubOrgClient.

        Verifies that:
          - The correct organization and repos payloads are returned.
          - The method filters repos correctly based on a specified license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("nonexistent_license"), [])

    def test_public_repos_with_license(self):
        """
        Integration test for public_repos with a specified license.

        Verifies that the method returns only repositories that match the
        specified license type.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("nonexistent_license"), [])
        self.assertEqual(client.public_repos("apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """
        Teardown resources after all tests in the class have completed.
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
