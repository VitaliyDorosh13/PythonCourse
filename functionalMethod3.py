def inner():
    print("Im function func()")

def outer(function):
    function()

outer(inner)

'''
Here’s what’s happening in the above example:

The call on line 9 passes inner() as an argument to outer().
Within outer(), Python binds inner() to the function parameter function.
outer() can then call inner() directly via function.
'''