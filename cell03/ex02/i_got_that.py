txt1 = str(input("What you gotta say? :"))
if txt1 != "STOP":
    txt = input("I got that! Anything else? :")
    while txt != "STOP":
        txt = input("I got that! Anything else? :")
        if txt == "STOP":
            break