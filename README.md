# Movie Trailer Site
This site showcases movies with their trailers. 

Have a quick peek from the following link
https://cdn.rawgit.com/theBeacon/ml-movie-trailer/1336a1cf/fresh_tomatoes.html

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
Append a or more movies' metadata to `movie.csv` in format specified and re-run the above command.
