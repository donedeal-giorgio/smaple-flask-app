from typing import List

from models import Movie, db


def get_movie(title: str) -> Movie:
    """
    Get a movie by title
    :param str title: the title of the movie

    :return: Movie
    """
    movie = Movie.query.filter_by(title=title).first()
    return movie


def add_movie(title: str) -> None:
    """
    Add a movie by providing a title
    :param title: the title of the movie
    """
    movie = Movie(title=title)
    db.session.add(movie)
    db.session.commit()


def get_all_movies() -> List[Movie]:
    """
    Get a list of all movies
    :return: list of movies
    """
    movies = Movie.query.all()
    return movies


def update_movie(new_title: str, old_title: str) -> None:
    """
    Update a movie by title
    :param new_title: old title
    :param old_title:  new title
    """
    movie = Movie.query.filter_by(title=old_title).first()
    movie.title = new_title
    db.session.commit()


def delete_movie(title: str) -> None:
    """
    Delete a movie by title
    :param title: the title of the movie to delete
    """
    movie = Movie.query.filter_by(title=title).first()
    db.session.delete(movie)
    db.session.commit()


def delete_all_movies() -> None:
    """
    Delete all movies
    """
    db.session.query(Movie).delete()
    db.session.commit()
