import webbrowser

"""create a website to show my favorite movies"""


class Movie():
    def __init__(self, movie_title, poster_image_url, trailer_youtube_id):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id

    def open_website(self):
        # change default website as Chrome
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = self.trailer_youtube_id
        webbrowser.get(chrome_path).open(url)