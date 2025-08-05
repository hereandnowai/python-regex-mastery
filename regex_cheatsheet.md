# Python Regex Cheatsheet

A quick reference guide for Python's `re` module.

## Basic Metacharacters

| Character | Description | Example |
| :--- | :--- | :--- |
| `.` | Matches any character except a newline. | `a.b` matches "acb" |
| `^` | Matches the start of the string. | `^Hello` matches "Hello world" |
| `$` | Matches the end of the string. | `world$` matches "Hello world" |
| `*` | Matches the preceding element zero or more times. | `ab*c` matches "ac", "abc", "abbc" |
| `+` | Matches the preceding element one or more times. | `ab+c` matches "abc", "abbc" |
| `?` | Matches the preceding element zero or one time. | `ab?c` matches "ac", "abc" |
| `{m}` | Matches the preceding element exactly `m` times. | `a{3}` matches "aaa" |
| `{m,n}` | Matches the preceding element from `m` to `n` times. | `a{2,4}` matches "aa", "aaa", "aaaa" |
| `[]` | Matches any single character within the brackets. | `[abc]` matches "a", "b", or "c" |
| `|` | Acts as an OR operator. | `a|b` matches "a" or "b" |
| `()` | Groups expressions and captures the matched text. | `(a|b)c` matches "ac" or "bc" |

## Special Sequences

Special sequences start with `\` and are used to match predefined sets of characters.

| Sequence | Description |
| :--- | :--- |
| `\d` | Matches any decimal digit; equivalent to `[0-9]`. |
| `\D` | Matches any non-digit character; equivalent to `[^0-9]`. |
| `\s` | Matches any whitespace character; equivalent to `[ \t\n\r\f\v]`. |
| `\S` | Matches any non-whitespace character; equivalent to `[^ \t\n\r\f\v]`. |
| `\w` | Matches any alphanumeric character; equivalent to `[a-zA-Z0-9_]`. |
| `\W` | Matches any non-alphanumeric character; equivalent to `[^a-zA-Z0-9_]`. |
| `\b` | Matches the empty string, but only at the beginning or end of a word. |
| `\B` | Matches the empty string, but not at the beginning or end of a word. |
| `\A` | Matches only at the start of the string. |
| `\Z` | Matches only at the end of the string. |

## Character Sets

| Set | Description |
| :--- | :--- |
| `[abc]` | Matches "a", "b", or "c". |
| `[a-c]` | Matches "a", "b", or "c". |
| `[^abc]` | Matches any character except "a", "b", or "c". |
| `[a-zA-Z]` | Matches any letter from "a" to "z" or "A" to "Z". |

## Groups and Capturing

| Construct | Description |
| :--- | :--- |
| `( ... )` | Captures the matched substring. |
| `(?: ... )` | Non-capturing group. |
| `(?P<name> ... )` | Named capturing group. |
| `(?P=name)` | Backreference to a named group. |
| `\number` | Backreference to a numbered group. |

## Lookarounds

Lookarounds are zero-width assertions that check for a match but don't consume any characters.

| Construct | Description |
| :--- | :--- |
| `(?= ... )` | Positive lookahead. Asserts that the text ahead matches. |
| `(?! ... )` | Negative lookahead. Asserts that the text ahead does not match. |
| `(?<= ... )` | Positive lookbehind. Asserts that the text behind matches. |
| `(?<! ... )` | Negative lookbehind. Asserts that the text behind does not match. |

## Flags

Flags modify the behavior of the regex engine.

| Flag | Short Form | Description |
| :--- | :--- | :--- |
| `re.IGNORECASE` | `re.I` | Makes the pattern case-insensitive. |
| `re.MULTILINE` | `re.M` | `^` and `$` match the start and end of each line. |
| `re.DOTALL` | `re.S` | `.` matches any character, including newlines. |
| `re.VERBOSE` | `re.X` | Allows for whitespace and comments within the pattern. |
| `re.ASCII` | `re.A` | `\w`, `\W`, `\b`, `\B`, `\s`, `\S` perform ASCII-only matching. |

## Common `re` Module Functions

| Function | Description |
| :--- | :--- |
| `re.match(pattern, string)` | Matches the pattern at the beginning of the string. |
| `re.search(pattern, string)` | Scans through the string looking for the first location where the pattern produces a match. |
| `re.findall(pattern, string)` | Returns a list of all non-overlapping matches in the string. |
| `re.finditer(pattern, string)` | Returns an iterator yielding match objects over all non-overlapping matches. |
| `re.sub(pattern, repl, string)` | Replaces occurrences of the pattern in the string with `repl`. |
| `re.compile(pattern)` | Compiles a regular expression pattern into a regex object for efficiency. |

## Common Patterns

| Use Case | Pattern |
| :--- | :--- |
| Email | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` |
| URL | `^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*/?$` |
| IP Address | `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$` |
| Date (YYYY-MM-DD) | `^\d{4}-\d{2}-\d{2}$` |
| Time (HH:MM:SS) | `^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$` |
