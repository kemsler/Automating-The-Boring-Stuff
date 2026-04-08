# Chapter 1

## Operators

| Operator | Operation                    | Example   | Evaluates to... |
|----------|------------------------------|-----------|-----------------|
| **       | Exponent                     | 2 ** 3    | 8               |
| %        | Modulus/remainder            | 22 % 8    | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                     | 22 / 8    | 2.75            |
| *        | Multiplication               | 3 * 5     | 15              |
| -        | Subtraction                  | 5 - 2     | 3               |
| +        | Addition                     | 2 + 2     | 4               |

## Data Types

| Data type              | Examples                                   |
|------------------------|--------------------------------------------|
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                   |
| Floating-point numbers | -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25     |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'      |

## Variables

A variable is like a box in the computer’s memory where you can store a  
single value. If you want to use the result of an evaluated expression later in  
your program, you can save it inside a variable.

### Assignment Statements

You’ll store values in variables with an assignment statement. An assignment  
statement consists of a variable name, an equal sign (called the assignment  
operator), and the value to be stored. If you enter the assignment statement  
spam = 42, then a variable named spam will have the integer value 42 stored in it.

### Variable names

You can name a variable anything as long as it obeys the following three rules:  
1. It can be only one word.  
2. It can use only letters, numbers, and the underscore (_) character.  
3. It can’t begin with a number.

#### Valid and Invalid variable names

| Valid variable names | Invalid variable names |
|----------------------|------------------------|
| balance | current-balance (hyphens are not allowed) |
| currentBalance | current balance (spaces are not allowed) |
| current_balance | 4account (can’t begin with a number) |
| _spam | 42 (can’t begin with a number) |
| SPAM | total_$um (special characters like $ are not allowed) |
| account4 | 'hello' (special characters like ' are not allowed) |

[!NOTE]
Text and Number Equivalence

Although the string value of a number is considered a completely different value from the integer or floating-point version, an integer can be equal to a floating point.

>>> 42 == '42'
False

>>> 42 == 42.0
True

>>> 42.0 == 0042.000
True

Python makes this distinction because strings are text, while integers and floats are both numbers.