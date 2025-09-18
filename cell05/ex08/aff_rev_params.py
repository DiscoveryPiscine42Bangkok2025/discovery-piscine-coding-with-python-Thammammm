text = input("Enter words separated by space: ").strip()

if not text or len(text.split()) < 2:
    print("none")
else:
    words = text.split()
    for word in reversed(words):
        print(word)