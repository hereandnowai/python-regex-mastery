"""
test_advanced.py

Pytest-based tests for the advanced regex concepts in advanced.py.
"""

import pytest
import re
from src.advanced import (
    demonstrate_backreferences,
    demonstrate_regex_for_validation,
    demonstrate_performance_tuning,
)

# Mock print statements for testing output
from unittest.mock import patch
import io

def test_demonstrate_backreferences():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_backreferences()
        output = fake_stdout.getvalue()

    assert "Matches: ['fox', 'apple', 'banana']" in output # For repeated words
    assert "Matches: ['tag', 'another']" in output # For named backreferences

def test_demonstrate_regex_for_validation():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_regex_for_validation()
        output = fake_stdout.getvalue()

    # Email validation checks
    assert "'test@example.com': Valid" in output
    assert "'user.name@sub.domain.co.uk': Valid" in output
    assert "'invalid-email': Invalid" in output
    assert "'@domain.com': Invalid" in output
    assert "'user@.com': Invalid" in output

    # Phone number validation checks
    assert "'123-456-7890': Valid" in output
    assert "'123.456.7890': Valid" in output
    assert "'123 456 7890': Valid" in output
    assert "'1234567890': Valid" in output
    assert "'123-45-67890': Invalid" in output

def test_demonstrate_performance_tuning():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_performance_tuning()
        output = fake_stdout.getvalue()

    assert "Using re.compile() for pattern '\bword\b' (case-insensitive):" in output
    assert "Matches: ['word', 'WORD']" in output
    assert "Avoid Catastrophic Backtracking" in output
    assert "Use `(?:...)` instead of `(...)` if you don't need to capture the group." in output

