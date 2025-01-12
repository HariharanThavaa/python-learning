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

- [ ] String Methods

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