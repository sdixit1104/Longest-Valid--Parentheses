# Longest Valid Parentheses

## Problem Statement

Given a string containing only the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

---

## Examples

### Example 1

**Input**
```text
(()
```

**Output**
```text
2
```

**Explanation**

The longest valid parentheses substring is "()".

---

### Example 2

**Input**
```text
)()())
```

**Output**
```text
4
```

**Explanation**

The longest valid parentheses substring is "()()".

---

### Example 3

**Input**
```text

```

**Output**
```text
0
```

---

## Approach

This solution uses a stack to store the indices of parentheses.

1. Initialize the stack with `-1`.
2. Traverse the string from left to right.
3. If the current character is `'('`, push its index onto the stack.
4. If the current character is `')'`, pop the top element from the stack.
5. If the stack becomes empty, push the current index as the new base.
6. Otherwise, calculate the length of the current valid substring and update the maximum length.

---

## Project Structure

```text
Longest-Valid-Parentheses/
│
├── LongestValidParen.py
├── README.md
└── screenshots/
    ├── output1.png
    └── output2.png
```

---

## Time Complexity

- O(n)

## Space Complexity

- O(n)

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Longest-Valid-Parentheses.git
```

2. Open the project directory.

```bash
cd Longest-Valid-Parentheses
```

3. Run the program.

```bash
python LongestValidParen.py
```

4. Enter the input string when prompted.

Example:

```text
Input:
(()())

Output:
6
```

---

## Screenshots

The `screenshots` folder contains sample output screenshots of the program execution.

---

## Author

Sumit Dixit.