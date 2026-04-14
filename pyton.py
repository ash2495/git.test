setattr(obj, 'attribute_name', 'value')
setattr(obj, 'attribute_name', value)
# Example
class MyClass:
    pass            
obj = MyClass()
nfjskl = 'Hello, World!'
setattr(obj, 'greeting', nfjskl)
print(obj.greeting)  # Output: Hello, World!
# Example with a function
def my_function():
    return "This is a function."
setattr(obj, 'my_method', my_function)
print(obj.my_method())  # Output: This is a function.
global_variable = "I am a global variable."
setattr(obj, 'global_var', global_variable)
print(obj.global_var)  # Output: I am a global variable.
