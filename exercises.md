# Regex Mastery Exercises

This document contains hands-on practice problems for each level of the Regex Mastery Tutorial. Work through them to solidify your understanding of regular expressions in Python.

---

## 📝 Basic Exercises

**Objective:** Practice `re.match`, `re.search`, `re.findall`, `re.split`, `re.sub`, character classes, and quantifiers.

### Exercise 1: Find Digits

**Task:** Extract all sequences of digits from a given string.

**Input:**
```
text = "The year is 2023, and the temperature is 25 degrees Celsius. My lucky number is 7."
```

**Expected Output:**
```
['2023', '25', '7']
```

### Exercise 2: Validate Start and End

**Task:** Check if a string starts with "Hello" and ends with "World".

**Input:**
```python
text1 = "Hello Python World"
text2 = "Hello World"
text3 = "Python World"
```

**Expected Output:**
```
text1: False
text2: True
text3: False
```

### Exercise 3: Replace Vowels

**Task:** Replace all vowels (a, e, i, o, u, case-insensitive) in a string with an asterisk `*`.

**Input:**
```
text = "Programming is fun and challenging."
```

**Expected Output:**
```
"Pr*gr*mm*ng *s f*n *nd ch*ll*ng*ng."
```

### Exercise 4: Split by Punctuation

**Task:** Split a sentence into words, using spaces, commas, periods, and exclamation marks as delimiters. Remove empty strings from the result.

**Input:**
```
sentence = "Hello, world! How are you today?"
```

**Expected Output:**
```
['Hello', 'world', 'How', 'are', 'you', 'today']
```

---

## 🧠 Intermediate Exercises

**Objective:** Practice using groups, named groups, lookarounds, greedy vs lazy matching, and flags.

### Exercise 5: Extract User Info

**Task:** From a log entry, extract the username, action, and timestamp using capturing groups.

**Input:**
```
log_entry = "[2023-10-26 14:35:01] User 'alice' performed 'login'."
```

**Expected Output:**
```
Username: alice
Action: login
Timestamp: 2023-10-26 14:35:01
```

### Exercise 6: Parse HTML Tags (Lazy)

**Task:** Extract the content within all `<b>` tags from an HTML snippet. Ensure your regex is lazy to avoid matching across multiple tags.

**Input:**
```html
html_snippet = "<p>This is <b>important</b> and also <b>urgent</b> information.</p>"
```

**Expected Output:**
```
['important', 'urgent']
```

### Exercise 7: Find Words Not Followed by a Specific Word

**Task:** Find all words that are *not* immediately followed by the word "bad".

**Input:**
```
text = "This is a good day. This is a bad idea. Another good thing."
```

**Expected Output:**
```
['This', 'is', 'a', 'good', 'day', 'This', 'is', 'a', 'idea', 'Another', 'good', 'thing']
```

### Exercise 8: Case-Insensitive Search

**Task:** Find all occurrences of the word "python" (case-insensitive) in a given text.

**Input:**
```
text = "Python is great. I love python. Learning PYTHON is fun."
```

**Expected Output:**
```
['Python', 'python', 'PYTHON']
```

---

## 🚀 Advanced Exercises

**Objective:** Practice backreferences, and regex for validation.

### Exercise 9: Find Repeated Words

**Task:** Find any word that is immediately repeated (e.g., "hello hello", "cat cat").

**Input:**
```
text = "The cat sat on the mat. Hello hello world. This is a test test."
```

**Expected Output:**
```
['hello', 'test']
```

### Exercise 10: Validate Simple Email Address

**Task:** Create a regex to validate a simple email address format (e.g., `name@domain.com`). It should have a username, an '@' symbol, a domain name, and a top-level domain (at least 2 characters).

**Input:**
```python
emails = [
    "test@example.com",
    "user.name@sub.domain.co",
    "invalid-email",
    "@domain.com",
    "user@.com",
    "user@domain"
]
```

**Expected Output (True/False for each):
```
test@example.com: True
user.name@sub.domain.co: True
invalid-email: False
@domain.com: False
user@.com: False
user@domain: False
```

### Exercise 11: Extract Hashtags

**Task:** Extract all hashtags (words starting with `#`) from a tweet. Hashtags can contain letters, numbers, and underscores.

**Input:**
```
tweet = "This is a #great day for #learning #Python_Regex! #AI"
```

**Expected Output:**
```
['#great', '#learning', '#Python_Regex', '#AI']
```

---

## 💡 Solutions

Solutions to these exercises can be found in `solutions.py`.
