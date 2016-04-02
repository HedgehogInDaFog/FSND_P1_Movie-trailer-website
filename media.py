class Movie():
    """This class contains data about movies, which will be shown at the webpage

    Attributes:
        title (str): Title of the movie
        storyline (str): Storyline of the movie
        poster_image (str): Link to the poster image
        trailer_youtube (str): Link to the trailer on the Youtube
        year (int): Year, the movie was released
        director (str): Director of the movie
        IMDB_rating (str): Rating of the movie in IMDB
        stars (list): List os strings. Every item is an actor
    """
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube, year, director, IMDB_rating, stars=[]):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.director = director
        self.IMDB_rating = IMDB_rating
        self.stars = stars
