import webbrowser
class Movie():

    def __init__(self, movie_title, movie_story_line, poster_image, youtube_trailer):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)