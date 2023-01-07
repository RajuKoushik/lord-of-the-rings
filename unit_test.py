import unittest
from lord_of_the_rings import Movie

class TestMovieMethods(unittest.TestCase):
    def setUp(self):
        self.movie = Movie()

    def test_get_all_movies(self):
        movies = self.movie.get_all_movies()
        self.assertIsInstance(movies, list)
        self.assertGreater(len(movies), 0)

    def test_get_movie_by_id(self):
        movie = self.movie.get_movie_by_id(1)
        self.assertIsInstance(movie, dict)
        self.assertEqual(movie['_id'], '5a1b8c1b06a6a4261f9b9491')

    def test_get_movie_quotes(self):
        quotes = self.movie.get_movie_quotes(1)
        self.assertIsInstance(quotes, list)
        self.assertGreater(len(quotes), 0)

if __name__ == '__main__':
    unittest.main()
