# Python Enigma

A simplified simulation of the historic Enigma cipher machine written in Python.

## Features

✅ Three rotating rotors

✅ Plugboard (Steckerbrett)

✅ Fixed reflector

✅ Object-oriented design

✅ Character transformation using ord() and chr()

✅ Support for German umlauts (Ä → AE, Ö → OE, Ü → UE, ß → SS)

Because every German encryption machine deserves proper umlaut support. 😄

---

## Project Structure

```text
.
├── main.py
└── mystery_box.py
```

---

## How It Works

The encryption path follows the same principle as the historic Enigma machine:

```text
Input
  ↓
Plugboard
  ↓
Rotor 1
  ↓
Rotor 2
  ↓
Rotor 3
  ↓
Reflector
  ↓
Rotor 3
  ↓
Rotor 2
  ↓
Rotor 1
  ↓
Plugboard
  ↓
Output
```

---

## Example

Input:

```text
Rotor 1: 5
Rotor 2: 17
Rotor 3: 3

Plugboard: AB

Text:
HELLO WORLD
```

Output:

```text
...
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Dictionaries
- String Manipulation
- Classes and Methods
- Exception Handling

---

## Learning Objectives

This project was developed as part of a Python Advanced course and demonstrates concepts from:

- Modules and Packages
- String Processing
- Exceptions
- Object-Oriented Programming

---

## Author

Sebastian Bochmann