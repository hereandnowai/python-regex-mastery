"""
test_basics.py

Pytest-based tests for the basic regex operations in basics.py.
"""

import pytest
import re
from src.basics import (
    demonstrate_match,
    demonstrate_search,
    demonstrate_findall,
    demonstrate_split,
    demonstrate_sub,
)

def test_demonstrate_match():
    # Test a successful match at the beginning
    match = demonstrate_match("Hello World", "^Hello")
    assert match is not None
    assert match.group() == "Hello"

    # Test no match (pattern not at beginning)
    match = demonstrate_match("World Hello", "^Hello")
    assert match is None

    # Test a partial match (should still return match object)
    match = demonstrate_match("HelloWorld", "Hello")
    assert match is not None
    assert match.group() == "Hello"

def test_demonstrate_search():
    # Test a successful match anywhere
    match = demonstrate_search("Hello World", "World")
    assert match is not None
    assert match.group() == "World"

    # Test no match
    match = demonstrate_search("Hello Python", "Java")
    assert match is None

    # Test match at the beginning
    match = demonstrate_search("Start here", "^Start")
    assert match is not None
    assert match.group() == "Start"

def test_demonstrate_findall():
    # Test finding all occurrences
    matches = demonstrate_findall("apple, banana, cherry, date", "a.+?e")
    assert matches == ['apple', 'date']

    # Test with numbers
    matches = demonstrate_findall("The price is $10.50 and $20.00.", r"\$\d+\.\d{2}")
    assert matches == ['$10.50', '$20.00']

    # Test no matches
    matches = demonstrate_findall("no numbers here", r"\d+")
    assert matches == []

def test_demonstrate_split():
    # Test splitting by multiple delimiters
    parts = demonstrate_split("apple,banana;cherry-date", r"[,;-]")
    assert parts == ['apple', 'banana', 'cherry', 'date']

    # Test splitting by whitespace
    parts = demonstrate_split("One two   three", r"\s+")
    assert parts == ['One', 'two', 'three']

    # Test splitting with no match
    parts = demonstrate_split("no_delimiter_here", r"[;]")
    assert parts == ['no_delimiter_here']

def test_demonstrate_sub():
    # Test simple replacement
    new_text = demonstrate_sub("The color is red.", "red", "blue")
    assert new_text == "The color is blue."

    # Test replacing a pattern
    new_text = demonstrate_sub("My phone number is 123-456-7890.", r"\d{3}-\d{3}-\d{4}", "[REDACTED]")
    assert new_text == "My phone number is [REDACTED]."

    # Test no replacement needed
    new_text = demonstrate_sub("No change here.", "xyz", "abc")
    assert new_text == "No change here."

