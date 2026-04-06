""" def square(items):
    for i, x in enumerate(items):
        items[i] = x * x  # Modify items in-place
a = [1, 2, 3, 4, 5]
obj = enumerate(a)  # Output: <enumerate object at 0x...>
print(a)  # Output: [1, 2, 3, 4, 5]
square(a)  # Changes a to [1, 4, 9, 16, 25]
print(a)  # Output: [1, 4, 9, 16, 25]

d = {} """

d = {0: 'polkovniju', 100: 'nikto', 200: 'ne', 2: 'pishet'}
print(f'old dict: {d}')  # Output: old dict: {0: 'polkovniju', 100: 'nikto', 200: 'ne', 2: 'pishet'}
d = {i: v for i, (_, v) in enumerate(d.items())}
print(f'new dict: {d}')  # Output: new dict: {0: 'polkovniju', 1: 'nikto', 2: 'ne', 3: 'pishet'}

print("\n\nGlobals", globals())  # Output: <module 'builtins' (built-in)>
print("\n\nLocals", locals())
print("\n\nLocals", locals()['__name__'])  # Output: {'d': {0: 'polkovniju


