from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(testing_config: dict = False) -> Flask:
    """
    Create a flask App
    :param testing_config:
    :return:
    """
    app = Flask(__name__, instance_relative_config=False)

    if not testing_config:
        app.config.from_object('config.Config')
    else:
        print("testing")
        app.config.from_mapping(testing_config)

    db.init_app(app)

    with app.app_context():
        import routes
        db.create_all()
        return app
