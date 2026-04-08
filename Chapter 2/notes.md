# Chapter 2 - Flow control

## Comparison operators

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| <  | Less than |
| >  | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

### The Difference Between the `==` and `=` Operators

You might have noticed that the `==` operator (**equal to**) has two equal signs,
while the `=` operator (**assignment**) has just one equal sign. It’s easy to
confuse these two operators with each other. Just remember these points:

- The `==` operator (**equal to**) asks whether two values are the same as each other.
- The `=` operator (**assignment**) puts the value on the right into the variable on the left.

To help remember which is which, notice that the `==` operator (**equal to**)
consists of two characters, just like the `!=` operator (**not equal to**)
consists of two characters.

## Boolean operators

The and and or operators always take two Boolean values (or expressions),  
so they’re considered binary operators. The and operator evaluates an expres-  
sion to True if both Boolean values are True; otherwise, it evaluates to False.  
Enter some expressions using and into the interactive shell to see it in action.

### The *and* Operator's Truth Table

| Expression       | Evaluates to... |
|------------------|-----------------|
| True and True    | True            |
| True and False   | False           |
| False and True   | False           |
| False and False  | False           |

### The *or* Operator's Truth Table

| Expression      | Evaluates to... |
|-----------------|-----------------|
| True or True    | True            |
| True or False   | True            |
| False or True   | True            |
| False or False  | False           |

### The *not* Operator's Truth Table

| Expression | Evaluates to... |
|------------|-----------------|
| not True   | False           |
| not False  | True            |

## Blocks of Code

Lines of Python code can be grouped together in **blocks**. You can tell when a
block begins and ends from the indentation of the lines of code. There are three
rules for blocks:

1. Blocks begin when the indentation increases.
2. Blocks can contain other blocks.
3. Blocks end when the indentation decreases to zero or to a containing block’s indentation.

Blocks are easier to understand by looking at some indented code, so let’s find
the blocks in part of a small game program, shown here:

```python
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
```
