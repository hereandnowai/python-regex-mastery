solutions.py

This module provides working solutions to the regex exercises defined in exercises.md.

import re

# --- Basic Exercises Solutions ---

def solve_exercise_1(text):
    """
    Solution for Exercise 1: Find Digits
    Task: Extract all sequences of digits from a given string.
    """
    return re.findall(r'\d+', text)

def solve_exercise_2(text):
    """
    Solution for Exercise 2: Validate Start and End
    Task: Check if a string starts with "Hello" and ends with "World".
    """
    return bool(re.match(r'^Hello.*World$', text))

def solve_exercise_3(text):
    """
    Solution for Exercise 3: Replace Vowels
    Task: Replace all vowels (a, e, i, o, u, case-insensitive) in a string with an asterisk `*`.
    """
    return re.sub(r'[aeiouAEIOU]', '*', text)

def solve_exercise_4(sentence):
    """
    Solution for Exercise 4: Split by Punctuation
    Task: Split a sentence into words, using spaces, commas, periods, and exclamation marks as delimiters.
          Remove empty strings from the result.
    """
    # Split by one or more of the specified delimiters
    parts = re.split(r'[ ,.!?]+', sentence)
    # Filter out any empty strings that might result from multiple delimiters or leading/trailing delimiters
    return [part for part in parts if part]

# --- Intermediate Exercises Solutions ---

def solve_exercise_5(log_entry):
    """
    Solution for Exercise 5: Extract User Info
    Task: From a log entry, extract the username, action, and timestamp using capturing groups.
    """
    pattern = r"..\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] User '(?P<username>.*?)' performed '(?P<action>.*?)'."
    match = re.search(pattern, log_entry)
    if match:
        return {
            "username": match.group("username"),
            "action": match.group("action"),
            "timestamp": match.group("timestamp")
        }
    return None

def solve_exercise_6(html_snippet):
    """
    Solution for Exercise 6: Parse HTML Tags (Lazy)
    Task: Extract the content within all `<b>` tags from an HTML snippet.
          Ensure your regex is lazy to avoid matching across multiple tags.
    """
    # <b.*?>: Matches <b> tag lazily
    # (.*?): Lazily captures content inside the tag
    # </b>: Matches closing </b> tag
    return re.findall(r'<b>(.*?)</b>', html_snippet)

def solve_exercise_7(text):
    """
    Solution for Exercise 7: Find Words Not Followed by a Specific Word
    Task: Find all words that are *not* immediately followed by the word "bad".
    """
    # \b(\w+)\b: Captures a whole word
    # (?!
    # \s+bad\b): Negative lookahead to ensure it's not followed by " bad"
    return re.findall(r'\b(\w+)\b(?!
    # \s+bad\b)', text)

def solve_exercise_8(text):
    """
    Solution for Exercise 8: Case-Insensitive Search
    Task: Find all occurrences of the word "python" (case-insensitive) in a given text.
    """
    return re.findall(r'python', text, re.IGNORECASE)

# --- Advanced Exercises Solutions ---

def solve_exercise_9(text):
    """
    Solution for Exercise 9: Find Repeated Words
    Task: Find any word that is immediately repeated (e.g., "hello hello", "cat cat").
    """
    # (\b\w+): Captures a whole word
    # \s+: Matches one or more spaces
    # \1: Backreference to the first captured group
    return re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)

def solve_exercise_10(email):
    """
    Solution for Exercise 10: Validate Simple Email Address
    Task: Create a regex to validate a simple email address format.
    """
    # ^: Start of string
    # [a-zA-Z0-9._%+-]+: Username part (one or more allowed chars)
    # @: Literal @ symbol
    # [a-zA-Z0-9.-]+: Domain name part (one or more allowed chars)
    # \.: Literal dot
    # [a-zA-Z]{2,}: Top-level domain (at least 2 letters)
    # $: End of string
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def solve_exercise_11(tweet):
    """
    Solution for Exercise 11: Extract Hashtags
    Task: Extract all hashtags (words starting with `#`) from a tweet.
    """
    # #:
    # Literal hash symbol
    # [a-zA-Z0-9_]+: One or more word characters (letters, numbers, underscore)
    return re.findall(r'#([a-zA-Z0-9_]+)', tweet)


if __name__ == "__main__":
    print("--- Solutions to Regex Mastery Exercises ---")

    # Basic Exercises Tests
    print("\n--- Basic Exercises ---")
    print(f"Ex 1: {solve_exercise_1("The year is 2023, and the temperature is 25 degrees Celsius. My lucky number is 7.")}")
    print(f"Ex 2 ('Hello Python World'): {solve_exercise_2("Hello Python World")}")
    print(f"Ex 2 ('Hello World'): {solve_exercise_2("Hello World")}")
    print(f"Ex 2 ('Python World'): {solve_exercise_2("Python World")}")
    print(f"Ex 3: {solve_exercise_3("Programming is fun and challenging.")}")
    print(f"Ex 4: {solve_exercise_4("Hello, world! How are you today?")}")

    # Intermediate Exercises Tests
    print("\n--- Intermediate Exercises ---")
    print(f"Ex 5: {solve_exercise_5("[2023-10-26 14:35:01] User 'alice' performed 'login'.")}")
    print(f"Ex 6: {solve_exercise_6("<p>This is <b>important</b> and also <b>urgent</b> information.</p>")}")
    print(f"Ex 7: {solve_exercise_7("This is a good day. This is a bad idea. Another good thing.")}")
    print(f"Ex 8: {solve_exercise_8("Python is great. I love python. Learning PYTHON is fun.")}")

    # Advanced Exercises Tests
    print("\n--- Advanced Exercises ---")
    print(f"Ex 9: {solve_exercise_9("The cat sat on the mat. Hello hello world. This is a test test.")}")
    emails_to_test = [
        "test@example.com",
        "user.name@sub.domain.co",
        "invalid-email",
        "@domain.com",
        "user@.com",
        "user@domain"
    ]
    print("Ex 10 Email Validation:")
    for email in emails_to_test:
        print(f"  '{email}': {solve_exercise_10(email)}")
    print(f"Ex 11: {solve_exercise_11("This is a #great day for #learning #Python_Regex! #AI")}")
