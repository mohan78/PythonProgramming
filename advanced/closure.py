"""
    A closure is a function object that remembers the data in enclosed scopes. To know more about
    closure, we need to know about types of scopes in Python. There are 3 types of scopes in python
    Built-in, Global, Local, Non-Local or Enclosing scope.

    1. Built-in scope: This is the widest scope. This consist of all the names that are loaded when
    we start the interpreter.
    
    2. Global: When a variable are defined in the script not inside any conditional, loops or functional
    namespace, then it is called to be a Global variable and the namespace is called Global namespace.
    Global variables can be accessed from anywhere in the script. A global variable can be created using
    keyword 'global'.

    3. Local: When a variable are defined in a loop or condition block or function namespace, then it is
    called to be local variable and it is called Local namespace.
    
    4. Non-Local or Enclosing: When a variable is defined in a nested function it is called non-local
    variable and the scope is called enclosing scope. This variable will neither have global or local scope.
    a Non-Local variable can be created using the keyword 'nonlocal'.
"""

global_x = 10 # This is a global variable

print(f"Value of global variable 'global_x' is {global_x}") # Output: 10
print("\n")


def func_1():
    # To be able to change the value of a global variable inside a function, we need to declare it as
    # a global variable.
    print("-"*30, "In func_1", "-"*30)
    global global_x
    print(f"Value of global variable 'global_x' inside func_1 is {global_x}")
    global_x = 20
    print("-"*30, "End of func_1", "-"*30, "\n")


def func_2():
    # A variable declared inside a function consists of local scope. It will not be available to access
    # outside this function
    print("-"*30, "In func_2", "-"*30)
    local_x = 10
    print(f"Value of local variable 'local_x' is {local_x}")  # Output: 10
    print("-"*30, "End of func_2", "-"*30, "\n")


def func_3():
    # In this, there is a nested function nested_func defined inside func_3. That nested function also
    # consists of another local_x which is redefined with value of 30.
    print("-"*30, "In func_3", "-"*30)
    local_x = 10

    def nested_func():
        local_x = 30
        print(f"Value of local variable 'local_x' inside nested_func is {local_x}")

    nested_func()
    print(f"Value of local variable 'local_x' inside func_3 is {local_x}")
    print("-"*30, "End of func_3", "-"*30, "\n")


def func_4():
    print("-"*30, "In func_4", "-"*30)
    local_x = 10
    print(f"Value of local variable 'local_x' inside func_4 is {local_x}")

    def nested_func():
        # Here we defined local_x is defined with nonlocal keyword meaning setting its scope to nonlocal
        # Hence this variable will same as the local_x variable defined in above func_4. Therefore changing
        # its value here will reflect in func_4's local_x.
        nonlocal local_x
        local_x = 30
    
    nested_func()
    print(f"Value of local variable 'local_x' inside func_4 after executing nested_func is {local_x}")

    print("-"*30, "End of func_4", "-"*30, "\n")


def func_5():
    print("-"*30, "In func_5", "-"*30)
    local_x = 10
    print(f"Value of local variable 'local_x' inside func_5 is {local_x}")

    def nested_func():
        # We can access local variable local_x inside nested_func even though it is not supplied to
        # nested_func as an argument. This is called 'Closure'.
        print(f"Value of variable 'local_x' accessed inside nested_func is {local_x}")
    
    nested_func()
    print("-"*30, "End of func_5", "-"*30, "\n")


func_1()
func_2()
func_3()
func_4()
func_5()
print(f"Value of global variable global_x after re-assignment in func_1 is {global_x}") # Output: 20
