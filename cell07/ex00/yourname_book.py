def array_of_names(persons):
    full_names = []
    
    for first_name, last_name in persons.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
      "fifi": "brindacier",
        "phuwish" : "prakobchit"
    }
    print(array_of_names(persons))