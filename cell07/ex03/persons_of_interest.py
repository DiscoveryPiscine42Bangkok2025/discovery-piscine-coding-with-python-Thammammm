def famous_births(historical_figures):
    sorted_figures = sorted(historical_figures.values(), key=lambda x: x['date_of_birth'])
    

    for figure in sorted_figures:
        name = figure['name']
        birth_year = figure['date_of_birth']
        print(f"{name} is a great scientist born in {birth_year}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)