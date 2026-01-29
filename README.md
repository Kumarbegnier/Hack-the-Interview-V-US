# Hack the Interview V (U.S.)

## Received Text – Keyboard Simulation Problem

This repository contains a **Python 3 solution** to the **“Received Text”** problem from  
**Hack the Interview V (U.S.)**.

The task is to simulate a keyboard with special keys and determine the final text
received after processing all keystrokes.

---

## Problem Summary

While typing an email, some special keys are pressed accidentally.
Given a string representing keystrokes, compute the final text output.

---

## Special Keys

| Key | Description |
|---|---|
| `<` | Move cursor to beginning (Home) |
| `>` | Move cursor to end (End) |
| `*` | Backspace |
| `#` | Toggle Num Lock |

### Rules
- Letters and `_` are always typed
- Digits are typed only when Num Lock is ON
- Cursor starts at the end
- Num Lock is ON initially

---

## Approach

The solution simulates a text editor using two lists:

[left text] | cursor | [right text]


This allows efficient cursor movement and backspace operations.
The input is processed **recursively**, one character at a time.

---

## Example

**Input**

HE*<LL>O


**Output**

LLHO


---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Note

Recursion is used for clarity and learning purposes.
For production systems, an iterative solution is recommended.

---

## Author

**Neeraj Kumar**  
AI • Machine Learning • Robotics • Datascience 
YouTube: **@ECEResearcher**



