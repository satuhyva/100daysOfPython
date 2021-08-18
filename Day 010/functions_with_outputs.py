def my1():
    return 3 + 2

print(my1())

def format_name(first, second):
    if first == '' or second == '':
        # this will return None
        return
    return first.title() + ' ' + second.title()

print(format_name('angela', 'wu'))
# print(format_name(input("1: "), input("2: ")))



# DOCSTINGS
def some_Function(input):
    """ 
    This function prints the input that it is given.
    Note: this docstring can contain several lines!
    Now HOVER OVER the function name!
    """
    print(input)

some_Function('DOCSTRINGS ARE COOL!')

"""
This is a comment, will not be treated as a docstring.
Because this is no connected to anything!
"""

some_variable = 222
""" This does not work. Variables cannot be documented! """
