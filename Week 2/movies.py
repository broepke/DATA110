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

# add a new horror movie
# first create a dictionary
newTitle = { "title": "Midsommar",
        "year": 2019,
        "rating": 7.1,
      }

# add the new title to horror. Note the use of append for lists
horror.append(newTitle)

# add another title, notice shorter code.
horror.append({ "title": "The Invisible Man",
        "year": 2020,
        "rating": 7.2,
      })

# add animation genre to the movies dictionary
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

# add more genres with movie titles

# display details of each genre
genres = moviesDict['movies']
for gen in genres:
  print(gen)
  movies = moviesDict['movies'][gen]

  # add remaining code to get the average rating movies by genre.
  # hint: use inner for-loop to loop through each movie of movies

  
