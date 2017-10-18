# Movie Trailer Site
This site showcases movies with their trailers.


## Prerequisite 
* Python 2.7
    * unicodecsv
    * webbrowser

## Behavior 
Site loads movie by reading metadata provided by `movie.csv` then webpage showcasing movies in the structure provided by `fresh_tomatoes.py`

## Structure
* `movie_center.py` links the all the code pieces together and entry point of the application.
* `fresh_tomatoes.py` provides backbone of the webpage.
* `movie.py` class Movie : represents the movie metadata.
* `util.py` holds code to read csv.

## Running the site
```python movie_center.py```

## Adding a new movie
Add a movie metadata in `movie.csv` and re-run the above command.