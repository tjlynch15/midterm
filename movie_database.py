#movie_database.py
import csv

class Movie:

    def find_highest_rated(filename):

        all_movies = []

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
        


            for row in reader:
                if row:
                    new_movie = Movie()
                    new_movie.title = row[1]
                    new_movie.imdb_rating = float(row[3])
                    new_movie.director = row[2]
                    all_movies.append(new_movie)


            highest = float(all_movies[0].imdb_rating)
            # print(highest)
            for movie in all_movies:
                # print(float((movie.imdb_rating)))

                if float(movie.imdb_rating) > highest:
                    highest = float(movie.imdb_rating)
                    highest_movie = movie


        return highest_movie



 # `http://www.omdbapi.com/?i={IMDB_MOVIE_ID}&plot=short&r=json`

 #   Example:
 #   http://www.omdbapi.com/?i=tt0076759&plot=short&r=json


        



# print(Movie.find_highest_rated('imdb_top250.csv'))