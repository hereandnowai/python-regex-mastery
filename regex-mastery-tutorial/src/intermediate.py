"""
intermediate.py

This module delves into intermediate regular expression concepts in Python,
including grouping, named groups, lookarounds, greedy vs. lazy matching,
and the use of regex flags.
"""

import re

def demonstrate_groups():
    """
    Demonstrates capturing groups using parentheses `()`.
    """
    print("\n--- Capturing Groups ---\n")
    text = "Name: John Doe, Age: 30, City: New York"
    pattern = r"Name: (.*), Age: (\d+), City: (.*)"
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")

    match = re.search(pattern, text)
    if match:
        print(f"Full match: {match.group(0)}") # Group 0 is the entire match
        print(f"Name: {match.group(1)}")
        print(f"Age: {match.group(2)}")
        print(f"City: {match.group(3)}")
        print(f"All groups as a tuple: {match.groups()}")
    else:
        print("No match found.")
    # Real-world: Extracting structured data from log files or configuration strings.

def demonstrate_named_groups():
    """
    Demonstrates named capturing groups using `?P<name>...`.
    """
    print("\n--- Named Capturing Groups ---\n")
    text = "Date: 2023-10-26, Event: Meeting, Location: Office A"
    pattern = r"Date: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}), Event: (?P<event>.*), Location: (?P<location>.*)"
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")

    match = re.search(pattern, text)
    if match:
        print(f"Full match: {match.group(0)}")
        print(f"Year: {match.group('year')}")
        print(f"Month: {match.group('month')}")
        print(f"Day: {match.group('day')}")
        print(f"Event: {match.group('event')}")
        print(f"Location: {match.group('location')}")
        print(f"All named groups as a dictionary: {match.groupdict()}")
    else:
        print("No match found.")
    # Real-world: Improving readability and maintainability when extracting multiple pieces of data.

def demonstrate_lookarounds():
    """
    Demonstrates positive/negative lookahead and lookbehind assertions.
    Lookarounds assert a condition without consuming characters.
    """
    print("\n--- Lookarounds (Assertions) ---\n")

    text = "I have $100 and 50 euros. The price is 25 USD."

    # Positive Lookahead (?=...): Matches if pattern is followed by ...
    # Find numbers followed by 'euros'
    pattern_pl = r"\b\d+\b(?=\s*euros)"
    print(f"Text: '{text}'")
    print(f"Pattern (Positive Lookahead): '{pattern_pl}' (numbers followed by 'euros')")
    print(f"Matches: {re.findall(pattern_pl, text)}")
    # Real-world: Finding specific values that precede or follow certain keywords.

    # Negative Lookahead (?!...): Matches if pattern is NOT followed by ...
    # Find numbers NOT followed by 'euros'
    pattern_nl = r"\b\d+\b(?!\s*euros)"
    print(f"\nPattern (Negative Lookahead): '{pattern_nl}' (numbers NOT followed by 'euros')")
    print(f"Matches: {re.findall(pattern_nl, text)}")
    # Real-world: Excluding specific patterns, e.g., finding words not in a blacklist.

    text2 = "PrefixValueSuffix"
    # Positive Lookbehind (?<=...): Matches if pattern is preceded by ...
    # Find 'Value' preceded by 'Prefix'
    pattern_pb = r"(?<=Prefix)Value"
    print(f"\nText: '{text2}'")
    print(f"Pattern (Positive Lookbehind): '{pattern_pb}' ('Value' preceded by 'Prefix')")
    print(f"Match: {re.search(pattern_pb, text2).group() if re.search(pattern_pb, text2) else 'No match'}")

    # Negative Lookbehind (?<!...): Matches if pattern is NOT preceded by ...
    # Find 'Value' NOT preceded by 'BadPrefix'
    pattern_nb = r"(?<!BadPrefix)Value"
    print(f"\nPattern (Negative Lookbehind): '{pattern_nb}' ('Value' NOT preceded by 'BadPrefix')")
    print(f"Match: {re.search(pattern_nb, text2).group() if re.search(pattern_nb, text2) else 'No match'}")

def demonstrate_greedy_vs_lazy():
    """
    Demonstrates the difference between greedy and lazy quantifiers.
    By default, quantifiers are greedy (match as much as possible).
    Adding '?' after a quantifier makes it lazy (match as little as possible).
    """
    print("\n--- Greedy vs. Lazy Quantifiers ---\n")

    html_text = "<p>This is a <b>bold</b> text.</p><p>Another <b>bold</b> section.</p>"

    # Greedy: .* matches as much as it can, often going beyond the intended match.
    # It will match from the first '<' to the last '>'.
    greedy_pattern = r"<.*>"
    print(f"Text: '{html_text}'")
    print(f"Greedy Pattern: '{greedy_pattern}'")
    print(f"Matches (Greedy): {re.findall(greedy_pattern, html_text)}")

    # Lazy: .*? matches as little as possible.
    # It will match each '<...>' tag individually.
    lazy_pattern = r"<.*?>"
    print(f"\nLazy Pattern: '{lazy_pattern}'")
    print(f"Matches (Lazy): {re.findall(lazy_pattern, html_text)}")
    # Real-world: Parsing XML/HTML tags, extracting content between delimiters.

def demonstrate_flags():
    """
    Demonstrates the use of regex flags to modify matching behavior.
    """
    print("\n--- Regex Flags ---\n")

    # re.IGNORECASE (re.I): Performs case-insensitive matching.
    text_case = "Hello World, hello python"
    pattern_case = r"hello"
    print(f"Text: '{text_case}'")
    print(f"Pattern: '{pattern_case}'")
    print(f"Matches (no flag): {re.findall(pattern_case, text_case)}")
    print(f"Matches (re.IGNORECASE): {re.findall(pattern_case, text_case, re.IGNORECASE)}")
    # Real-world: Searching for keywords regardless of their casing.

    # re.MULTILINE (re.M): Makes ^ and $ match the start/end of each line, not just the string.
    text_multiline = "Line 1\nLine 2\nLine 3"
    pattern_multiline = r"^Line"
    print(f"\nText:\n'{text_multiline}'")
    print(f"Pattern: '{pattern_multiline}'")
    print(f"Matches (no flag): {re.findall(pattern_multiline, text_multiline)}") # Only matches start of string
    print(f"Matches (re.MULTILINE): {re.findall(pattern_multiline, text_multiline, re.MULTILINE)}") # Matches start of each line
    # Real-world: Parsing line-by-line data in multi-line strings.

    # re.DOTALL (re.S): Makes '.' match any character, including newline.
    text_dotall = "First line\nSecond line"
    pattern_dotall = r"First.*Second"
    print(f"\nText:\n'{text_dotall}'")
    print(f"Pattern: '{pattern_dotall}'")
    print(f"Match (no flag): {re.search(pattern_dotall, text_dotall)}") # No match because . doesn't match newline
    print(f"Match (re.DOTALL): {re.search(pattern_dotall, text_dotall, re.DOTALL).group() if re.search(pattern_dotall, text_dotall, re.DOTALL) else 'No match'}")
    # Real-world: Matching patterns that span across multiple lines.


if __name__ == "__main__":
    print("--- Intermediate Regex Concepts in Python ---")
    demonstrate_groups()
    demonstrate_named_groups()
    demonstrate_lookarounds()
    demonstrate_greedy_vs_lazy()
    demonstrate_flags()
