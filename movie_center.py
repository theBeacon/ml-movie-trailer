"""
This module integrates all the pieces together to wield the website
"""

import util
from fresh_tomatoes import open_movies_page
from movie import Movie


def main():
    """ load the movies meta-data from the csv and \
        objectify them and showcase the site """

    # load the movies
    raw_movies = util.read_csv('movie.csv')

    # make movies objects
    movies = []
    for raw_movie in raw_movies:
        movie_genres = [] if 'genres' not in raw_movie \
                      else raw_movie['genres'].split('|')

        movies.append(Movie(raw_movie['title'],
                      raw_movie['poster'],
                      raw_movie['trailer'],
                      movie_genres))
    # open the webpage with movies
    open_movies_page(movies)

main()
