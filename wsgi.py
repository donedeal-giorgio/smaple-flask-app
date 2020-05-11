import os

from app import create_app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(
        host=flask_app.config.get('FLASK_HOST'),
        port=flask_app.config.get('FLASK_PORT')
    )
