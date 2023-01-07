import requests

class Movie:
    BASE_URL = 'https://the-one-api.herokuapp.com/v2/movie'

    def get_all_movies(self):
        """
        Makes a GET request to the /movie endpoint and returns a list of movies.
        """
        response = requests.get(self.BASE_URL)
        if response.status_code != 200:
            raise Exception('An error occurred: {}'.format(response.text))
        return response.json()['docs']

    def get_movie_by_id(self, id):
        """
        Makes a GET request to the /movie/{id} endpoint and returns a movie object.
        """
        url = '{}/{}'.format(self.BASE_URL, id)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('An error occurred: {}'.format(response.text))
        return response.json()

    def get_movie_quotes(self, id):
        """
        Makes a GET request to the /movie/{id}/quote endpoint and returns a list of quotes.
        """
        url = '{}/{}/quote'.format(self.BASE_URL, id)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('An error occurred: {}'.format(response.text))
        return response.json()['docs']
