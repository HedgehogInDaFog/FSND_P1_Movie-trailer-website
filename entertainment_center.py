import media

movie_data = [
    {
    "title": "A Beautiful Mind",
    "storyline": "After a brilliant but asocial mathematician, John Nash, accepts secret work in cryptography, his life takes a turn for the nightmarish",
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMTQ4MDI2MzkwMl5BMl5BanBnXkFtZTYwMjk0NTA5._V1_UX182_CR0,0,182,268_AL_.jpg",
    "trailer_youtube": "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
    "year": 2011,
    "director":"Ron Howard",
    "IMDB_rating": "8,2",
    "stars": ["Russell Crowe", "Ed Harris", "Jennifer Connelly"]
    },

    {
    "title": "Lucky Number Slevin",
    "storyline": "A case of mistaken identity lands Slevin into the middle of a war being plotted by two of the city's most rival crime bosses: The Rabbi and The Boss. Slevin is under constant surveillance by relentless Detective Brikowski as well as the infamous assassin Goodkat and finds himself having to hatch his own ingenious plot to get them before they get him.",
    "poster_image": "http://ia.media-imdb.com/images/M/MV5BMzc1OTEwMTk4OF5BMl5BanBnXkFtZTcwMTEzMDQzMQ@@._V1_UY268_CR2,0,182,268_AL_.jpg",
    "trailer_youtube": "https://www.youtube.com/watch?v=fVIUEcizkPc",
    "year": 2006,
    "director":"Paul McGuigan",
    "IMDB_rating": "7,8",
    "stars": ["Josh Hartnett", "Ben Kingsley", "Morgan Freeman"]
    }
]

movies = []

for i in movie_data:
    movies.append(media.Movie(i["title"], i["storyline"], i["poster_image"], i["trailer_youtube"], i["year"], i["director"], i["IMDB_rating"], i["stars"]))

print movies
