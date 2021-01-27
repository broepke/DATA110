# =============================================================================
# 1. Create a function getTitle that asks for user input for
# (title, year, rating) and return a dictionary with the user values.
# Make sure to include exception handling of invalid input types.
#
# 2. Create a function displayMovies which takes a dictionary as an input
# parameter and prints the details of each movie genre, along with all
# movies within a genre.
#
# 3. Instead of defining a partially populated movie dictionary, you should
# start with an empty dictionary which gets added to given calls to getTitle.
#
# 4. Also instead of a static 5 genres, use while loop which terminate
# based on user input of  "quit" for genre.
# There will still be 5 movie titles per genre.
# =============================================================================


def getTitle():
    '''Function to populate a single movie dictionary'''

    keys = ['title', 'year', 'rating']
    values = []

    ok = False
    while not ok:
        title = input('Enter movie title: ')
        try:
            val = str(title)
            ok = True
            values.append(val)
        except ValueError:
            print("Invalid type. Please try again")

    ok = False
    while not ok:
        year = input('Enter movie year: ')
        try:
            val = int(year)
            ok = True
            values.append(val)
        except ValueError:
            print("Invalid type. Please try again")

    ok = False
    while not ok:
        rating = input("Enter movie rating: ")
        try:
            val = float(rating)
            ok = True
            values.append(val)
        except ValueError:
            print("Invalid type. Please try again")

    d = {k: v for k, v in zip(keys, values)}

    return d


def displayMovies(mov_dict):
    '''Print off the entire User entered movide dictionary'''

    genres = mov_dict['movies']
    for gen in genres:
        print(gen)
        total = 0
        count = 0
        for movies in genres[gen]:
            print(
                f"movie: {movies['title']}, year: "
                f"{movies['year']}, rating: {movies['rating']}")
            total += movies['rating']
            count += 1
        print(f"{gen} avg movie rating: {total/count}")
        print('')


# Globals
moviesDict = {"movies": {}}


# Ask the User for a Genre and 5 Movies
while True:
    # Get the Genre from the user or abort
    genre = input('Enter genre name or "QUIT" to exit: ')
    if genre.lower() == "quit":
        # If the user enters quit, then exit the while loop completely.
        break
    else:
        # Reset the list for each new genre iteration
        titles = []
        # Request the user enter 5 movie titles
        for i in range(5):
            user_title = getTitle()
            titles.append(user_title)

        moviesDict['movies'][genre] = titles


displayMovies(moviesDict)
