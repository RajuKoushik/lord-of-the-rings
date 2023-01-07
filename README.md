# Lord of the Rings SDK



This is an SDK for the Lord of the Rings API. It provides a simple interface for accessing movie data and quotes from the trilogy.

Installation
To install the SDK, run the following command:

```
pip install lord-of-the-rings
```
Usage
To use the SDK, import the Movie class and create an instance of it:

```
from lord_of_the_rings import Movie

movie = Movie()
```

You can then call the following methods on the movie object:

```
get_all_movies(): Returns a list of all movies in the trilogy.
get_movie_by_id(id): Returns a movie object for the movie with the specified id.
get_movie_quotes(id): Returns a list of quotes for the movie with the specified id.

```


Here is an example of how to use the SDK:

```
all_movies = movie.get_all_movies()
print(all_movies)

movie_by_id = movie.get_movie_by_id(id)
print(movie_by_id)

movie_quotes = movie.get_movie_quotes(id)
print(movie_quotes)
```

Dependencies
The SDK requires the following dependencies:

- requests


Development
To contribute to the development of the SDK, clone the repository and install the dependencies:

```
git clone https://github.com/RajuKoushik/lord-of-the-rings/sdk.git
pip install -r requirements.txt
```
