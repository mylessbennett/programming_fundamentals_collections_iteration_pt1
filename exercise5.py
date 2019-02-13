#Lists
fav_colours = ["teal", "orange", "red", "gold"]
ages = [23, 21, 24, 23, 14, 25]
coin_flip = ["tails", "heads", "heads", "tails", "tails"]
artists = ["J.cole","Chance the Rapper", "Lauryn Hill"]

#Dictionaries
words = {
    'crusade': 'a medieval military expedition',
    'majority': 'the greater number',
    'basketball': 'a game played between two teams of five players in which goals are scored by throwing a ball through a netted hoop fixed above each end of the court.'
}

fav_movies = {
    'friday night lights': 2004,
    'how the grinch stole christmas': 2000,
    'the dark knight': 2008,
}

cities_pop = {
    'toronto': 2700000,
    'miami': 463347,
    'barcelona': 1600000
}

names_and_ages = {
    'Alex': 21,
    'Jordan': 23,
    'Danielle': 24,
    'Tudor': 24,
    'Emma': 15
}
#---------------------------------------------------------------
total_population = 0
for keys, population in cities_pop.items():
    total_population = total_population + population
print(total_population)
#---------------------------------------------------------------
for name, age in names_and_ages.items():
    if age > 21:
        print("{} is old".format(name))
    else:
        print("{} is young".format(name))
#---------------------------------------------------------------
print(fav_colours[2:])
#---------------------------------------------------------------
for age in ages:
    print(age + 1)
#---------------------------------------------------------------
fav_colours.append('yellow')
fav_colours.append('blue')
print(fav_colours)
