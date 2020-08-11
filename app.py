from flask import Flask

from views.website import website
from views.user import user

BLUEPRINTS = [
    (website, ''),
    (user, '/user'),
]


def create_app():
    app = Flask(__name__)
    blueprints = BLUEPRINTS
    for view, url_prefix in blueprints:
        app.register_blueprint(view, url_prefix=url_prefix)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

