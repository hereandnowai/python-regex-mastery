# Regex Mastery Tutorial

## Overview

Welcome to the Regex Mastery Tutorial! This repository is designed to help you learn and master regular expressions (regex) in Python, from the absolute basics to advanced techniques. Whether you're looking to validate user input, parse complex log files, or extract specific information from text, understanding regex is a powerful skill for any developer.

## Learning Objectives

By the end of this tutorial, you will be able to:

- Understand the fundamental concepts of regular expressions.
- Use Python's `re` module effectively for various text processing tasks.
- Construct complex regex patterns using groups, lookarounds, and backreferences.
- Apply regex for common real-world problems like data validation and parsing.
- Optimize regex patterns for better performance.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/regex-mastery-tutorial.git
    cd regex-mastery-tutorial
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install pytest
    ```

## Table of Contents

- [Basics of Regex in Python](#basics-of-regex-in-python)
- [Intermediate Regex Concepts](#intermediate-regex-concepts)
- [Advanced Regex Techniques](#advanced-regex-techniques)
- [Hands-on Exercises](#hands-on-exercises)
- [Solutions](#solutions)

## Topics Covered

### Basics of Regex in Python

- `re.match`, `re.search`, `re.findall`, `re.split`, `re.sub`
- Character classes (`\d`, `\w`, `\s`, `.`)
- Quantifiers (`*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`)
- Anchors (`^`, `$`)

### Intermediate Regex Concepts

- Grouping and Capturing (`()`)
- Named Groups (`?P<name>...`)
- Lookarounds (Positive/Negative Lookahead/Lookbehind)
- Greedy vs. Lazy Quantifiers
- Regex Flags (`re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`)

### Advanced Regex Techniques

- Backreferences (`\1`, `\g<name>`)
- Recursive Patterns
- Regex for Validation (Emails, Phone Numbers, URLs)
- Performance Tuning and Debugging Regex

### Hands-on Exercises

Practical problems to test your understanding at each level.

### Solutions

Working solutions to all exercises for self-verification.