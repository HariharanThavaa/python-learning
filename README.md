## This is python learning

1. tuple: (name, house)
2. List: [name, house]
3. Dictionary: {"name": name, "house": house}
4. classes: class key word to declare
5. objects: Student()
6. attributes: instance variables
7. methods: behaviour
8. raise


#### Printing student object 
1. __str__
```
 def __str__(self):
        return f"{self.name} from {self.house}"
```

#### Type

```
print(type(50))
print(type("Hello World"))
print(type([]))
print(type(list()))
print(type({}))
print(type(dict()))
```

```
@HariharanThavaa ➜ /workspaces/python-learning/oop/ex-1 (main) $ python type.py
<class 'int'>
<class 'str'>
<class 'list'>
<class 'list'>
<class 'dict'>
<class 'dict'>
```

#### Class Method

@classmethod

@staticmethod

#### inheritance

```
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
```

#### Operator Overloading

https://docs.python.org/3/reference/datamodel.html#special-method-names