from flask import Flask

def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    from views.root import bp as root_bp
    app.register_blueprint(root_bp)
    return app

application = app = create_app('./config.py')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
