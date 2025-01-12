### Week01 : Functions

- [X] hello.py
- [X] Command-line Interface 
python hello.py
- [X] Python Interpretter
- [X] Functions, Arguments, Side effects

functions - print
arguments - "hello, world"
side effects - visual, audio anything

- [X] Bugs and Debugging

bugs - mistake 

- [X] VS Code and Integration Development Environment
- [X] Return Values and Variables

return values
variables

- [X] Comments and Psedocode

comments - notes in our code
pseudocode - TODO List for you / structuring your ideas before writing the code.

- [X] Multiple Function Arguments

- [X] Named Parameters

str - String (stir)
https://docs.python.org
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/functions.html#print

parameters - keys
arguments - values

end='\n' - new line
sep=' ' - separator space

positional parameters
names parameters

- [X] Escaping Character

print("hello, "friend"")

```
$ python hello.py 
  File "/workspaces/python-learning/W01_Functions/hello.py", line 2
    print("hello, "friend"")
          ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

couple of fixes.
1. print('hello, "friend"')
2. print("hello, \"friend\"")

- [X] f-strings

format string

- [X] String Methods

str
https://docs.python.org/3/library/stdtypes.html#string-methods

```python
# Remove whitespace from str
name = name.strip()

# capitalize the name
name = name.capitalize()
```
```
$ python hello.py 
What's your name?      hariharan       
Hello, Hariharan
```

Title

```
$ python hello.py 
What's your name?     hariharan thava
Hello, Hariharan Thava
```

chaining funtions

```
python hello.py 
What's your name?     hariharan thava   
Hello, Hariharan thava
```

name = name.strip().title()
get the value of the name
strip off the whitespace from both left and right
capitalize each word's first letter
then assign that value to name

- [X] Style
- [X] Split
- [X] Integesrs and Operators

int
+ - Add
- - subtract
* - multiply
/ - divide
% - Modulo

Interactive mode
```
$ python
Python 3.12.1 (main, Dec 12 2024, 22:30:56) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 1
2
>>> print("Hello, World")
Hello, World
>>> 
```

- [X] calculator.py

- [X] Type Coversion

int

- [ ] Floating Point Values

float  - Number with the decimal points

```
python calculator.py 
What's x? 1.2
What's y? 3.4
4.6
```

https://docs.python.org/3/library/functions.html#round
round(number, ndigits=None)¶