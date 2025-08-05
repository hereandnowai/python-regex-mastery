"""
test_intermediate.py

Pytest-based tests for the intermediate regex concepts in intermediate.py.
"""

import pytest
import re
from src.intermediate import (
    demonstrate_groups,
    demonstrate_named_groups,
    demonstrate_lookarounds,
    demonstrate_greedy_vs_lazy,
    demonstrate_flags,
)

# Mock print statements for testing output
from unittest.mock import patch
import io

def test_demonstrate_groups():
    text = "Name: John Doe, Age: 30, City: New York"
    pattern = r"Name: (.*), Age: (\d+), City: (.*)"

    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_groups()
        output = fake_stdout.getvalue()

    assert "Full match: Name: John Doe, Age: 30, City: New York" in output
    assert "Name: John Doe" in output
    assert "Age: 30" in output
    assert "City: New York" in output
    assert "All groups as a tuple: ('John Doe', '30', 'New York')" in output

def test_demonstrate_named_groups():
    text = "Date: 2023-10-26, Event: Meeting, Location: Office A"
    pattern = r"Date: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}), Event: (?P<event>.*), Location: (?P<location>.*)"

    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_named_groups()
        output = fake_stdout.getvalue()

    assert "Year: 2023" in output
    assert "Month: 10" in output
    assert "Day: 26" in output
    assert "Event: Meeting" in output
    assert "Location: Office A" in output
    assert "All named groups as a dictionary: {'year': '2023', 'month': '10', 'day': '26', 'event': 'Meeting', 'location': 'Office A'}" in output

def test_demonstrate_lookarounds():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_lookarounds()
        output = fake_stdout.getvalue()

    assert "Matches: ['100']" in output # Positive Lookahead for euros
    assert "Matches: ['50', '25']" in output # Negative Lookahead for euros
    assert "Match: Value" in output # Positive Lookbehind
    assert "Match: Value" in output # Negative Lookbehind

def test_demonstrate_greedy_vs_lazy():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_greedy_vs_lazy()
        output = fake_stdout.getvalue()

    assert "Matches (Greedy): ['<p>This is <b>bold</b> text.</p><p>Another <b>bold</b> section.</p>"]" in output
    assert "Matches (Lazy): ['<p>', '<b>', '</b>', '</p>', '<p>', '<b>', '</b>', '</p>"]" in output

def test_demonstrate_flags():
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        demonstrate_flags()
        output = fake_stdout.getvalue()

    assert "Matches (no flag): ['hello']" in output
    assert "Matches (re.IGNORECASE): ['Hello', 'hello']" in output
    assert "Matches (no flag): ['Line']" in output
    assert "Matches (re.MULTILINE): ['Line', 'Line', 'Line']" in output
    assert "Match (no flag): None" in output
    assert "Match (re.DOTALL): First line\nSecond line" in output
