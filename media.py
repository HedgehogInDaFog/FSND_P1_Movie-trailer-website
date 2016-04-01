class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube, director="Unknown", budget="Unknown", stars=[]):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.budget = budget
        self.stars = stars
