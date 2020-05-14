from models import Movie, db
from typing import List


def get_movie(title: str) -> Movie:
    movie = Movie.query.filter_by(title=title).first()
    return movie


def add_movie(title: str) -> None:
    movie = Movie(title=title)
    db.session.add(movie)
    db.session.commit()


def get_all_movies() -> List[Movie]:
    movies = Movie.query.all()
    return movies


def update_movie(new_title: str, old_title: str) -> None:
    movie = Movie.query.filter_by(title=old_title).first()
    movie.title = new_title
    db.session.commit()


def delete_movie(title: str) -> None:
    movie = Movie.query.filter_by(title=title).first()
    db.session.delete(movie)
    db.session.commit()


def delete_all_movies() -> None:
    db.session.query(Movie).delete()
    db.session.commit()
