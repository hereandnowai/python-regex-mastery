"""
advanced.py

This module explores advanced regular expression techniques in Python,
including backreferences, recursion (conceptual), regex for validation
(emails, phone numbers), and performance tuning considerations.
"""

import re

def demonstrate_backreferences():
    """
    Demonstrates backreferences, which refer to a previously captured group.
    `\1` refers to the first captured group, `\2` to the second, and so on.
    `\g<name>` refers to a named captured group.
    """
    print("\n--- Backreferences ---\n")

    text = "The quick brown fox jumps over the lazy fox. apple apple, banana banana."

    # Find repeated words (e.g., "fox fox" or "apple apple")
    # (\w+): Captures a whole word.
    # \1: Refers to the content captured by the first group.
    pattern = r"\b(\w+)\s+\1\b"
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}' (finds repeated words)")
    print(f"Matches: {re.findall(pattern, text)}")
    # Real-world: Detecting duplicate words in text, finding balanced tags (simple cases).

    # Using named backreferences
    text_named = "<tag>content</tag> <another>stuff</another>"
    # (?P<word>\w+): Captures a word and names it 'word'.
    # \g<word>: Refers to the content captured by the named group 'word'.
    pattern_named = r"<(?P<tag_name>\w+)>.*?</\g<tag_name>>"
    print(f"\nText: '{text_named}'")
    print(f"Pattern: '{pattern_named}' (finds matching XML/HTML tags)")
    print(f"Matches: {re.findall(pattern_named, text_named)}")
    # Real-world: Validating matching HTML/XML tags, parsing structured data where opening and closing elements must match.

def demonstrate_regex_for_validation():
    """
    Demonstrates using regex for common data validation tasks.
    """
    print("\n--- Regex for Validation ---\n")

    # Email Validation (simplified for demonstration)
    # This pattern is a common example, but real-world email validation is very complex.
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = [
        "test@example.com",
        "user.name@sub.domain.co.uk",
        "invalid-email",
        "@domain.com",
        "user@.com"
    ]
    print("\n--- Email Validation ---")
    print(f"Pattern: '{email_pattern}'")
    for email in emails:
        is_valid = "Valid" if re.match(email_pattern, email) else "Invalid"
        print(f"'{email}': {is_valid}")
    # Real-world: Validating user input in forms, cleaning data.

    # Phone Number Validation (simplified for demonstration - e.g., North American format)
    # (\d{3}): three digits
    # [-.\]?: optional hyphen, dot, or space
    phone_pattern = r"^(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    phone_numbers = [
        "123-456-7890",
        "(123) 456-7890", # This pattern won't match parentheses, showing limitations/need for more complex patterns
        "123.456.7890",
        "123 456 7890",
        "1234567890",
        "123-45-67890" # Invalid length
    ]
    print("\n--- Phone Number Validation (NA Format) ---")
    print(f"Pattern: '{phone_pattern}'")
    for phone in phone_numbers:
        is_valid = "Valid" if re.match(phone_pattern, phone) else "Invalid"
        print(f"'{phone}': {is_valid}")
    # Real-world: Standardizing phone number formats, input validation.

def demonstrate_performance_tuning():
    """
    Discusses conceptual aspects of regex performance tuning.
    Actual benchmarking would require more extensive code.
    """
    print("\n--- Regex Performance Tuning (Conceptual) ---\n")
    print("1. **Be Specific:** Use specific character classes (e.g., \d instead of . if you know it's a digit).")
    print("2. **Avoid Catastrophic Backtracking:** This occurs with nested quantifiers like `(a+)+` or `(a|aa)*`.")
    print("   Example of problematic pattern: `(a+)+` on 'aaaaaaaaaaaaaaaaaaaaaaaaX'")
    print("   Use possessive quantifiers (not directly supported in Python's `re` module, but conceptual) or atomic groups.")
    print("   In Python, often rewriting the pattern or using `re.compile()` helps.")

    # Example of re.compile()
    compiled_pattern = re.compile(r"\bword\b", re.IGNORECASE)
    text_for_compile = "This is a word. Another WORD here."
    print(f"\nUsing re.compile() for pattern '\bword\b' (case-insensitive):")
    print(f"Matches: {compiled_pattern.findall(text_for_compile)}")
    # Real-world: Optimizing regex for high-volume text processing, log analysis.

    print("4. **Anchors:** Use `^` and `$` to anchor patterns to the start/end of strings/lines when appropriate.")
    print("5. **Non-capturing Groups:** Use `(?:...)` instead of `(...)` if you don't need to capture the group.")
    print("   This can offer a minor performance boost and clarifies intent.")


if __name__ == "__main__":
    print("--- Advanced Regex Techniques in Python ---")
    demonstrate_backreferences()
    demonstrate_regex_for_validation()
    demonstrate_performance_tuning()
