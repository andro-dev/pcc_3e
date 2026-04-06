'''

In Python, a namespace is essentially a mapping from names (identifiers) to objects. You can think of it as a dictionary where the keys are your variable or function names and the values are the actual objects they refer to. 
Real Python
Real Python
 +2
Core Purpose
The primary goal of namespaces is to prevent naming conflicts. Just as two different folders on your computer can each contain a file named data.csv without issue, two different namespaces in Python can contain a variable named x without them interfering with one another. 
Real Python
Real Python
 +3
Types of Namespaces
Python manages several levels of namespaces, each with a different lifetime: 
Built-in Namespace: Contains names always available in Python (e.g., print(), len(), ValueError). It is created when the interpreter starts and lasts until it exits.
Global Namespace: Created for each module your program loads. It contains names defined at the top level of a script or module and lasts until the interpreter terminates.
Local Namespace: Created whenever a function is called. It contains names defined inside that function and is typically destroyed once the function finishes executing.
Enclosing (Nonlocal) Namespace: Exists in "nested" scenarios, such as when one function is defined inside another. The inner function can see names from the outer function's namespace. 
Real Python
Real Python
 +4
How Name Resolution Works (LEGB Rule)
When you reference a name in your code, Python searches for it across these namespaces in a specific order known as the LEGB rule: 
Real Python
Real Python
 +1
Local: Inside the current function.
Enclosing: Inside any enclosing functions (from inner to outer).
Global: At the module level.
Built-in: Python's own internal names. 
If the name isn't found after checking all four, Python raises a NameError. 
Python Programming for Economics and Finance
Python Programming for Economics and Finance
Inspecting Namespaces
You can see these "dictionaries" yourself using built-in functions: 
locals(): Returns a dictionary of the current local namespace.
globals(): Returns a dictionary of the current global namespace.
dir(): Lists the names defined in the current or specified namespace. 

'''
# 1. Global Namespace
message = "Hello from Global!"

def outer_function():
    # 2. Enclosing Namespace (relative to inner_function)
    message = "Hello from Enclosing!"

    def inner_function():
        # 3. Local Namespace
        message = "Hello from Local!"
        
        # Python finds 'message' in the Local namespace first
        print(f"Inside inner_function: {message}")

    inner_function()
    
    # After inner_function finishes, we are back in the Enclosing namespace
    print(f"Inside outer_function: {message}")

# 4. Built-in Namespace
# 'len' is always available because it's in the built-in namespace
print(f"At module level: {message}")
outer_function()
print(f"Built-in example: {len(['a', 'b', 'c'])}")