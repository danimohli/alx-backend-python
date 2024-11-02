#!/usr/bin/env python3
"""
Unit tests for access_nested_map function in utils module.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map returns correct values.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError with correct message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Test case for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected result.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test case for memoize decorator.
    """

    def test_memoize(self):
        """
        Test that memoize caches result after first call.
        """

        class TestClass:
            def a_method(self):
                """
                Method returning a constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Memoized property that calls a_method.
                """
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance,
                          'a_method', return_value=42) as mock_method:
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
