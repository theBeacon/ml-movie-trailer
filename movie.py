"""
 This module holds the Movie class which represents meta-data of a movie.
"""

import re


class Movie():
    """Represents meta data of a Moive"""

    def __init__(self, title, poster_image_url, trailer_youtube_url, genres):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.genres = genres

    def get_youtube_id(self):
        """ Extract the youtube ID from the url """

        id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        id_match = id_match or re.search(
                                        r'(?<=be/)[^&#]+',
                                        self.trailer_youtube_url)
        trailer_youtube_id = (id_match.group(0) if id_match
                              else None)
        return trailer_youtube_id
