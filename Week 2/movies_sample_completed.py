'''
dictionary with movie genres from imdb
each genre is a list of dictionary objects
'''
moviesDict = { "movies": {
  # horror titles
    "horror": [
      { "title": "The Lodge",
        "year": 2019,
        "rating": 6.1,
      },
      { "title": "The Platform",
        "year": 2019,
        "rating": 7.0,
      },
    ],
    # comedy titles
    "comedy": [
      { "title": "Trolls World Tour",
        "year": 2020,
        "rating": 6.1
      }
    ],
  }
}

# returns all horror movies
horror = moviesDict["movies"].get("horror") 

# first create a dictionary
newTitle = { "title": "Midsommar",
        "year": 2019,
        "rating": 7.1,
      }

# add the new title to horror.
horror.append(newTitle)

horror.append({ "title": "The Invisible Man",
        "year": 2020,
        "rating": 7.2,
      })
horror.append({ "title": "Fantasy Island",
        "year": 2020,
        "rating": 4.8,
      })

comedies = moviesDict["movies"].get("comedy") 
comedies.append({ "title": "What We Do in the Shadows",
        "year": 2014,
        "rating": 7.7,
      })
comedies.append({ "title": "Fantasy Island",
        "year": 2020,
        "rating": 4.8,
      })
comedies.append({ "title": "Ready or Not (I)",
        "year": 2019,
        "rating": 6.8,
      })
comedies.append({ "title": "Bad Education (2019)",
        "year": 2019,
        "rating": 7.2
      })


# add animation genre
animations = [
      { "title": "The Willoughbys",
        "year": 2020,
        "rating": 6.4,
      },
       { "title": "Trolls World Tour",
        "year": 2020,
        "rating": 6.1,
      },
       { "title": "Onward (I)",
        "year": 2020,
        "rating": 7.5,
      },
       { "title": "The Lion King",
        "year": 2019,
        "rating": 6.9,
      },
       { "title": " Frozen II",
        "year": 2019,
        "rating": 7.0,
      },
    ]
moviesDict['movies']['animation'] = animations

# add drama genre
actions = [
      { "title": "Underwater",
        "year": 2020,
        "rating": 5.8,
      },
       { "title": "The Hunt (II)",
        "year": 2020,
        "rating": 6.4,
      },
       { "title": "Zombieland: Double Tap",
        "year": 2019,
        "rating": 6.8,
      },
       { "title": "Upgrade",
        "year": 2018,
        "rating": 7.5,
      },
       { "title": "Train to Busan",
        "year": 2016,
        "rating": 7.5,
      },
    ]
moviesDict['movies']['action'] = actions

# add action genre
dramas = [
      { "title": "Bad Education",
        "year": 2019,
        "rating": 7.2,
      },
       { "title": "365 Days",
        "year": 2020,
        "rating": 3.6,
      },
       { "title": "The Lodge",
        "year": 2019,
        "rating": 6.1,
      },
       { "title": "Once Upon a Time in Hollywood",
        "year": 2019,
        "rating": 7.7,
      },
       { "title": "Parasite",
        "year": 2019,
        "rating": 8.6,
      },
    ]
moviesDict['movies']['drama'] = dramas
 

# display details of each genre
genres = moviesDict['movies']
for gen in genres:
  print(gen)
  movies = moviesDict['movies'][gen]
  
  avgRating=0
  for m in movies:
      title = m['title']
      year = m['year']
      rating = m['rating']
      avgRating = avgRating + rating
      print(f'movie: {title}, year: {year}, rating: {rating}')
    
  avgRating = avgRating/ len(movies)
  print(f'{gen} avg movie rating: {avgRating}')
  print()
  

