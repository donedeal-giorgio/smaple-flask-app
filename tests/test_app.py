from services.moviemanager import *


def test_index(client):
	response = client.get("/")
	assert response.status_code == 200


def test_update(client, app):
	new_movie_title = 'this is an updated test'
	response = client.post("/update", data={'newtitle': new_movie_title, 'oldtitle': 'this is a test'})
	app.app_context().push()
	updated = get_movie(new_movie_title)
	assert response.status_code == 302
	assert updated
