from flask import Flask, request, abort, redirect
from flask_login import LoginManager, login_url
from model.config.session import get_session
from model.user.user import User

from views.website import website
from views.user import user
from views.lib import lib

BLUEPRINTS = [
    (website, ''),
    (user, '/user'),
    (lib, "/lib"),
]


def configure_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)
    app.config['SECRET_KEY'] = 'landsljklandsljk'

    @login_manager.user_loader
    def user_loader(user_id):
        with get_session() as db_session:
            u = db_session.query(User).get(user_id)
            return u

    @login_manager.unauthorized_handler
    def unauthorized():
        if not login_manager.login_view:
            abort(401)
        return redirect(login_url(login_manager.login_view, request.url))


def create_app():
    app = Flask(__name__)
    blueprints = BLUEPRINTS
    for view, url_prefix in blueprints:
        app.register_blueprint(view, url_prefix=url_prefix)
    configure_login_manager(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

