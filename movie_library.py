"""
Project Idea: "Movie Library"

Description: This project involves creating a movie library application. It will utilize object-oriented programming principles to manage movie data and perform 
operations such as adding, deleting, and updating movies in the library.

Project Features:

Create a class named Movie. This class will represent a movie and will have attributes like movie title, director, release year, and genre.

Create a class named MovieLibrary. This class will store movie objects and handle operations related to movies.

The MovieLibrary class should contain methods to add a new movie, delete a movie, update movie details, and list all the movies in the library.

Implement a user interface to interact with the movie library. The user should be able to add new movies, edit existing movies, and perform deletion operations.

Additionally, you can add a method to filter movies based on their genre. For example, the user should be able to list movies of a specific genre, such as "comedy."

This project will provide a great opportunity to practice object-oriented programming concepts. While managing movie data with classes and objects, adding a user
interface will make the application more user-friendly. Moreover, implementing features like data management and filtering will enhance your skills in creating more
complex applications.
"""


class Movie:
    def __init__(self, movie_title, director, release_year, genre):
        self.movie_title = movie_title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def get_movie(self):
        return {"movie title": self.movie_title,
                "director": self.director,
                "release year": self.release_year,
                "genre": self.genre
                }


class Library:
    def __init__(self):
        self.movies = []

    def add_movie(self):
        movie = Movie(

            input("title: "),
            input("director: "),
            input("release year: "),
            input("genre: ")
        )

        self.movies.append(movie)
        print("movie added.")

    def list_all_movies(self):
        for movie in self.movies:
            print(movie.get_movie())

    def remove_movie(self):
        search = input("enter the name of movie that you want to remove: ")
        found = False
        for movie in self.movies:
            if movie.movie_title == search:

                self.movies.remove(movie)
                found = True
                print("movie deleted.")

            if not found:
                print("Movie can not found.")

    def upgrade_movie(self):
        print(f"the movie list: {self.list_all_movies()} ")
        m = input("Please enter the name of movie that you want to upgrade: ")

        found = False

        for movie in self.movies:
            if m == movie.movie_title:
                attribute = input(
                    "which property do you want to change (movie_title, director, release_year, genre): ")
                new_value = input("Please enter the new value: ")

                setattr(movie, attribute, new_value)
                found = True
                print(f"{attribute} changing completed.")

        if not found:
            print("movie cannot found")

            # setattr(obj, attribute, value)

    def genre_filter(self):
        filtered_list = []
        found = False
        genre = input(
            "what kind of movie do you want to filter? Please be sure that you type right ")

        for movie in self.movies:
            if genre == movie.genre:
                filtered_list.append(movie)
                found = True

        if len(filtered_list) != 0:
            for movie in filtered_list:
                print(f"Movies: {movie.get_movie()}")
        if not found:
            print(f"there is no {genre} movie in library.")

    def release_year_filter(self):
        filtered_list = []
        found = False
        release_year = input(
            "Enter the release year. Please be sure that you type right ")

        for movie in self.movies:
            if release_year == movie.release_year:
                filtered_list.append(movie)
                found = True

        if len(filtered_list) != 0:
            for movie in filtered_list:
                print(f"Movies: {movie.get_movie()}")
        if not found:
            print(
                f"there is no movie released in {release_year} in library library.")

    def director_filter(self):
        filtered_list = []
        found = False
        director = input(
            "Enter the director. Please be sure that you type right ")

        for movie in self.movies:
            if director == movie.director:
                filtered_list.append(movie)
                found = True

        if len(filtered_list) != 0:
            for movie in filtered_list:
                print(f"Movies: {movie.get_movie()}")
        if not found:
            print(f"there is no {director} movie in library.")


my_library = Library()

my_library.add_movie()
my_library.add_movie()
my_library.add_movie()
my_library.list_all_movies()

my_library.upgrade_movie()
my_library.genre_filter()
