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

print(fav_colours[len(fav_colours) - 1])
#---------------------------------------------------------------
cities_pop['prague'] = 1200000
#---------------------------------------------------------------
coin_flip_reversed = coin_flip.reverse()
#---------------------------------------------------------------
print(cities_pop['miami'])
#---------------------------------------------------------------
for artist in artists:
    print("I think {} is great".format(artist))
