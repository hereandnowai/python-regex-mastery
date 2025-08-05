basics.py

This module covers the fundamental concepts of regular expressions in Python.
It introduces basic regex operations using the `re` module, including searching,
matching, finding all occurrences, splitting strings, and substituting patterns.


import re

def demonstrate_match(text, pattern):
    """
    Demonstrates re.match(): Checks for a match only at the beginning of the string.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to match.

    Returns:
        re.Match object or None: The match object if found, otherwise None.
    """
    print(f"\n--- re.match() ---")
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    match = re.match(pattern, text)
    if match:
        print(f"Match found from index {match.start()} to {match.end()}: '{match.group()}'")
    else:
        print("No match found at the beginning of the string.")
    return match

def demonstrate_search(text, pattern):
    """
    Demonstrates re.search(): Scans through string looking for the first location
    where the regex pattern produces a match.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to search for.

    Returns:
        re.Match object or None: The match object if found, otherwise None.
    """
    print(f"\n--- re.search() ---")
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    match = re.search(pattern, text)
    if match:
        print(f"First match found from index {match.start()} to {match.end()}: '{match.group()}'")
    else:
        print("No match found anywhere in the string.")
    return match

def demonstrate_findall(text, pattern):
    """
    Demonstrates re.findall(): Finds all non-overlapping matches of pattern in string,
    returning them as a list of strings.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to find.

    Returns:
        list: A list of all found matches.
    """
    print(f"\n--- re.findall() ---")
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    matches = re.findall(pattern, text)
    print(f"All matches found: {matches}")
    return matches

def demonstrate_split(text, pattern):
    """
    Demonstrates re.split(): Splits the string by the occurrences of pattern.

    Args:
        text (str): The string to split.
        pattern (str): The regex pattern to split by.

    Returns:
        list: A list of strings resulting from the split.
    """
    print(f"\n--- re.split() ---")
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    parts = re.split(pattern, text)
    print(f"Split parts: {parts}")
    return parts

def demonstrate_sub(text, pattern, repl):
    """
    Demonstrates re.sub(): Replaces occurrences of pattern in string with repl.

    Args:
        text (str): The original string.
        pattern (str): The regex pattern to replace.
        repl (str): The replacement string.

    Returns:
        str: The string after replacement.
    """
    print(f"\n--- re.sub() ---")
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    print(f"Replacement: '{repl}'")
    new_text = re.sub(pattern, repl, text)
    print(f"New text: '{new_text}'")
    return new_text

def demonstrate_character_classes():
    """
    Demonstrates common character classes.
    """
    print("\n--- Character Classes ---")
    text = "The quick brown fox jumps over 12 lazy dogs."
    print(f"Text: '{text}'")

    # \d: Matches any digit (0-9)
    print(f"\nPattern: '\d' (digits)")
    print(f"Matches: {re.findall(r'\d', text)}") # Real-world: Extracting numbers from text

    # \w: Matches any word character (alphanumeric + underscore)
    print(f"\nPattern: '\w+' (word characters)")
    print(f"Matches: {re.findall(r'\w+', text)}") # Real-world: Tokenizing words

    # \s: Matches any whitespace character (space, tab, newline, etc.)
    print(f"\nPattern: '\s' (whitespace)")
    print(f"Matches: {re.findall(r'\s', text)}") # Real-world: Splitting text by spaces

    # .: Matches any character (except newline by default)
    print(f"\nPattern: 'o.' (o followed by any character)")
    print(f"Matches: {re.findall(r'o.', text)}") # Real-world: Simple pattern matching

def demonstrate_quantifiers():
    """
    Demonstrates common quantifiers.
    """
    print("\n--- Quantifiers ---")
    text = "aaabbcdeeeffg"
    print(f"Text: '{text}'")

    # *: Zero or more occurrences
    print(f"\nPattern: 'a*' (zero or more 'a's)")
    print(f"Matches: {re.findall(r'a*', text)}") # Note: Matches empty strings between other chars

    # +: One or more occurrences
    print(f"\nPattern: 'a+' (one or more 'a's)")
    print(f"Matches: {re.findall(r'a+', text)}") # Real-world: Finding consecutive identical characters

    # ?: Zero or one occurrence
    print(f"\nPattern: 'b?' (zero or one 'b')")
    print(f"Matches: {re.findall(r'b?', text)}") # Real-world: Optional characters in a pattern

    # {n}: Exactly n occurrences
    print(f"\nPattern: 'e{{3}}' (exactly three 'e's)")
    print(f"Matches: {re.findall(r'e{3}', text)}") # Real-world: Fixed length codes

    # {n,}: n or more occurrences
    print(f"\nPattern: 'f{{1,}}' (one or more 'f's)")
    print(f"Matches: {re.findall(r'f{1,}', text)}") # Same as 'f+'

    # {n,m}: Between n and m occurrences (inclusive)
    print(f"\nPattern: 'a{{1,3}}' (between 1 and 3 'a's)")
    print(f"Matches: {re.findall(r'a{1,3}', text)}") # Real-world: Flexible length patterns

def demonstrate_anchors():
    """
    Demonstrates anchors.
    """
    print("\n--- Anchors ---")
    text1 = "Hello World"
    text2 = "World Hello"
    text3 = "Hello\nWorld"

    # ^: Matches the beginning of the string (or line in MULTILINE mode)
    print(f"\nText: '{text1}'")
    print(f"Pattern: '^Hello' (starts with 'Hello')")
    print(f"Match: {re.search(r'^Hello', text1).group() if re.search(r'^Hello', text1) else 'No match'}")

    print(f"Text: '{text2}'")
    print(f"Pattern: '^Hello'")
    print(f"Match: {re.search(r'^Hello', text2).group() if re.search(r'^Hello', text2) else 'No match'}")

    # $: Matches the end of the string (or line in MULTILINE mode)
    print(f"\nText: '{text1}'")
    print(f"Pattern: 'World$' (ends with 'World')")
    print(f"Match: {re.search(r'World$', text1).group() if re.search(r'World$', text1) else 'No match'}")

    print(f"Text: '{text2}'")
    print(f"Pattern: 'World$'")
    print(f"Match: {re.search(r'World$', text2).group() if re.search(r'World$', text2) else 'No match'}")

    # Real-world: Validating entire strings, e.g., a password must start with a letter and end with a digit.
    # Example with MULTILINE flag (covered in intermediate.py)
    print(f"\nText: '{text3}'")
    print(f"Pattern: '^World$' with re.MULTILINE")
    # In MULTILINE mode, ^ and $ match the start/end of each line
    match_multiline = re.search(r'^World$', text3, re.MULTILINE)
    print(f"Match: {match_multiline.group() if match_multiline else 'No match'}")


if __name__ == "__main__":
    print("--- Basic Regex Operations in Python ---")

    # re.match() examples
    demonstrate_match("Hello World", "Hello")
    demonstrate_match("World Hello", "Hello") # No match because it's not at the beginning

    # re.search() examples
    demonstrate_search("Hello World", "World")
    demonstrate_search("The quick brown fox", "quick")

    # re.findall() examples
    demonstrate_findall("apple, banana, cherry, date", "a.+e") # Greedy match
    demonstrate_findall("apple, banana, cherry, date", "a.+?e") # Non-greedy match (covered in intermediate)
    demonstrate_findall("The price is $10.50 and $20.00.", r"$\d+\.\d{2}")

    # re.split() examples
    demonstrate_split("apple,banana;cherry-date", r"[,;-]")
    demonstrate_split("One two   three", r"\s+")

    # re.sub() examples
    demonstrate_sub("The color is red.", "red", "blue")
    demonstrate_sub("My phone number is 123-456-7890.", r"\d{3}-\d{3}-\d{4}", "[REDACTED]")

    demonstrate_character_classes()
    demonstrate_quantifiers()
    demonstrate_anchors()
