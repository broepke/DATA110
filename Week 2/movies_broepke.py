'''
dictionary with movie genres from imdb
each genre is a list of dictionary objects
'''

moviesDict = {}
moviesDict['movies'] = {'horror': [
    {"title": None, "year": None, "rating": None}]}

# add horror genre to the movies dictionary
horror_films = [
    {"title": "The Lodge",
     "year": 2019,
        "rating": 6.1,
     },
    {"title": "The Platform",
        "year": 2019,
     "rating": 7.0,
     },
    {"title": "Midsommar",
        "year": 2019,
     "rating": 7.1,
     },
    {"title": "The Invisible Man",
        "year": 2020,
     "rating": 7.2,
     },
    {"title": "Alien",
        "year": 1979,
     "rating": 8.4,
     },
]
moviesDict['movies']['horror'] = horror_films

# add animation genre to the movies dictionary
animation_films = [
    {"title": "The Willoughbys",
     "year": 2020,
        "rating": 6.4,
     },
    {"title": "Trolls World Tour",
        "year": 2020,
     "rating": 6.1,
     },
    {"title": "Onward (I)",
        "year": 2020,
     "rating": 7.5,
     },
    {"title": "The Lion King",
        "year": 2019,
     "rating": 6.9,
     },
    {"title": "Frozen II",
        "year": 2019,
     "rating": 7.0,
     },
]
moviesDict['movies']['animation'] = animation_films

comedy_films = [
    {"title": "Back to the Future",
     "year": 1985,
        "rating": 8.5,
     },
    {"title": "Soul",
        "year": 2020,
     "rating": 8.1,
     },
    {"title": "Love Actually",
        "year": 2003,
     "rating": 7.6,
     },
    {"title": "Ocean's Eight ",
        "year": 2018,
     "rating": 6.8,
     },
    {"title": "Coming to America",
        "year": 1988,
     "rating": 7.0,
     },
]

moviesDict['movies']['comedy'] = comedy_films

# add more genres with movie titles
scifi_films = [
    {"title": "Avengers: Endgame",
     "year": 2019,
        "rating": 8.4,
     },
    {"title": "Interstellar",
        "year": 2014,
     "rating": 8.6,
     },
    {"title": "Avengers: Infinity War ",
        "year": 2018,
     "rating": 8.4,
     },
    {"title": "Inception",
        "year": 2010,
     "rating": 8.8,
     },
    {"title": "The Matrix",
        "year": 1999,
     "rating": 8.7,
     },
]
moviesDict['movies']['scifi'] = scifi_films

action_films = [
    {"title": "Wonder Woman 1984",
     "year": 2020,
        "rating": 5.5,
     },
    {"title": "Tenent",
        "year": 2020,
     "rating": 7.5,
     },
    {"title": "The Karate Kid",
        "year": 1984,
     "rating": 7.3,
     },
    {"title": "The Gentlemen",
        "year": 2019,
     "rating": 7.8,
     },
    {"title": "The Lord of the Rings: The Fellowship of the Ring",
        "year": 2001,
     "rating": 8.8,
     },
]

moviesDict['movies']['action'] = action_films

# display details of each genre
genres = moviesDict['movies']
for gen in genres:
    print(gen)
    total = 0
    count = 0
    for movies in genres[gen]:
        print("movie: {}, year: {}, rating: {}".format(
            movies['title'], movies['year'], movies['rating']))
        total += movies['rating']
        count += 1
    print('{} avg movie rating: {}'.format(gen, total/count))
    print('')
