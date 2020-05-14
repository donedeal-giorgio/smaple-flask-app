import os
import tempfile
import json
import pytest
from app import create_app
from models import db

with open(os.path.join(os.path.dirname(__file__), "resources/data.json"), "rb") as f:
	_mock_data = json.load(f)
	print(_mock_data)


# _data_sql = f.read().decode("utf8")


@pytest.fixture(scope="session")
def app():
	db_fd, db_path = tempfile.mkstemp()
	print(db_fd, db_path)
	# app = create_app(testing_config=True)

	app = create_app(
		{
			'SQLALCHEMY_DATABASE_URI': "sqlite:///{}".format(db_path),
			'TESTING': True,
			'DEBUG': True,
			'SQLALCHEMY_TRACK_MODIFICATIONS': False
		})
	with app.app_context():
		for title in _mock_data:
			db.session.execute("INSERT INTO movie(title) VALUES(:title)", title)
		db.session.commit()

	yield app
	print("-----------------")
	print("-----------------")
	print("-----------------")
	# close and remove the temporary database
	os.close(db_fd)
	os.unlink(db_path)


@pytest.fixture
def client(app):
	"""A test client for the app."""
	return app.test_client()


@pytest.fixture
def runner(app):
	"""A test runner for the app's Click commands."""
	return app.test_cli_runner()


@pytest.fixture
def database(app):
	return db
