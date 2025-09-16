def add_one(value):
    """Adds 1 to the parameter passed to the method."""
    return value + 1

my_variable = 5
print(f"Initial value: {my_variable}")

my_variable = add_one(my_variable)

print(f"Value after add_one: {my_variable}")