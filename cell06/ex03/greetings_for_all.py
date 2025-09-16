def greetings(name="noble stranger"):
    """Display a welcome message; default is 'noble stranger'."""
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)