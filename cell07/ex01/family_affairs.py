def find_the_redheads(family):
    
    redheads = list(filter(lambda name: family[name] == "red", family))
    return redheads

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))