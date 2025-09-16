i = 0
while i <= 10:
    multiply = ""
    j = 0
    while j <= 10:
        multiply += f" {i*j}"
        j += 1
    print(f"Table de {i} :{multiply}")
    i += 1