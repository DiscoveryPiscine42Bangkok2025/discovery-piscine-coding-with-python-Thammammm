import sys

def downcase_it(string):
    """Convert the given string to lowercase and return it."""
    return string.lower()

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        print(downcase_it(param))