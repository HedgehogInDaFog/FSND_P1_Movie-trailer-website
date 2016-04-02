from fresh_tomatoes import open_movies_page
import media

# Using a list of dictionaries for storing data about the movies. Every 
# item of a list contains data about single movie. This way allows to easily
# add new movies. Every dictionary MUST have all attributes (title, storyline,
# poster_image, trailer_youtube, year, director, IMDB_rating, stars)
movie_data = [{
    "title": "A Beautiful Mind",
    "storyline": '''After a brilliant but asocial mathematician,
                John Nash, accepts secret work in cryptography,
                his life takes a turn for the nightmarish''',
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMTQ4MDI2MzkwMl5BMl5BanBnXkFtZTYwMjk0NTA5._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
    "year": 2011,
    "director": "Ron Howard",
    "IMDB_rating": "8,2",
    "stars": ["Russell Crowe", "Ed Harris", "Jennifer Connelly"]
    },

    {
    "title": "Lucky Number Slevin",
    "storyline": ("A case of mistaken identity lands Slevin into the middle "
                "of a war being plotted by two of the city's most rival "
                "crime bosses: The Rabbi and The Boss. Slevin is under "
                "constant surveillance by relentless Detective Brikowski as"
                " well as the infamous assassin Goodkat and finds himself "
                "having to hatch his own ingenious plot to get them before "
                "they get him."),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMzc1OTEwMTk4OF5BMl5BanBnXkFtZTcwMTEzMDQzMQ@@._V1_UY268_CR2,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=fVIUEcizkPc",
    "year": 2006,
    "director": "Paul McGuigan",
    "IMDB_rating": "7,8",
    "stars": ["Josh Hartnett", "Ben Kingsley", "Morgan Freeman"]
    },

    {
    "title": "In Time",
    "storyline": ("In a future where people stop aging at 25, but are"
                " engineered to live only one more year, having the means to"
                " buy your way out of the situation is a shot at immortal "
                "youth. Here, Will Salas finds himself accused of murder and"
                " on the run with a hostage - a connection that becomes an "
                "important part of the way against the system. "),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMjA3NzI1ODc1MV5BMl5BanBnXkFtZTcwMzI5NjQwNg@@._V1_UY268_CR5,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=fdadZ_KrZVw",
    "year": 2011,
    "director": "Andrew Niccol",
    "IMDB_rating": "6,7",
    "stars": ["Justin Timberlake", "Amanda Seyfried", "Cillian Murphy"]
    },

    {
    "title": "Inception",
    "storyline": ("A thief, who steals corporate secrets through use of dream-"
                "sharing technology, is given the inverse task of planting "
                "an idea into the mind of a CEO."),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "year": 2010,
    "director": "Christopher Nolan",
    "IMDB_rating": "8,8",
    "stars": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },

    {
    "title": "Back to the Future",
    "storyline": ("A young man is accidentally sent thirty years into the "
                "past in a time-traveling DeLorean invented by his friend, "
                "Dr. Emmett Brown, and must make sure his high-school-age "
                "parents unite in order to save his own existence."),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=qvsgGtivCgs",
    "year": 1985,
    "director": "Robert Zemeckis",
    "IMDB_rating": "8,5",
    "stars": ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]
    },

    {
    "title": "Django Unchained",
    "storyline": ("With the help of a German bounty hunter, a freed slave "
                "sets out to rescue his wife from a brutal Mississippi "
                "plantation owner."),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=eUdM9vrCbow",
    "year": 2012,
    "director": "Quentin Tarantino",
    "IMDB_rating": "8,5",
    "stars": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio"]
    },

    {
    "title": "The Lord of the Rings: The Return of the King",
    "storyline": ("Gandalf and Aragorn lead the World of Men against Sauron's"
                " army to draw his gaze from Frodo and Sam as they approach "
                "Mount Doom with the One Ring."),
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "trailer_youtube": "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
    "year": 2003,
    "director": "Peter Jackson",
    "IMDB_rating": "8,9",
    "stars": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"]
    }
]

movies = []
for i in movie_data:
    movies.append(media.Movie(
                            i["title"], i["storyline"], i["poster_image"],
                            i["trailer_youtube"], i["year"], i["director"],
                            i["IMDB_rating"], i["stars"]
                            ))
open_movies_page(movies)
