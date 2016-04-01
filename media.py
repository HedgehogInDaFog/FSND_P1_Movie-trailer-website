class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube, year, director, IMDB_rating, stars=[]):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.director = director
        self.IMDB_rating = IMDB_rating
        self.stars = stars
