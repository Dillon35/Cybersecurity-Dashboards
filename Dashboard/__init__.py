import os

from flask import Flask, render_template



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('home.html')
    
    from . import home
    app.register_blueprint(home.home_bp)

    @app.after_request
    def close_mpl_plot(response):
        """This prevents memory leakage; Matplotlib's pyplot API is stateful, which
        can be a burden for a website that runs for a while.
        """
        import matplotlib.pyplot as plt
        plt.close('all')
        return response

    return app