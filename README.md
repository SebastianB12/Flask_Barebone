# Flask_Barebone
Minimal Flask Setup

Flask Barebone on PythonAnywhere
Flask is a lightweight …..

I use this Barbone for every Flask project as a starting point:
Projectfolder
    -app
        -main
        -static
        -templates
        -__init__.py
    -config.py
    -run.py


Let's go through all files to understand what happens in each file:

The starting file of the flask applicaiton in this case is "run.py" (It does not have to be named like that, it can has every name you want.)

run.py:
    #Import operating system functionalities
    import os 
    #import the create_app function from our __init__.py file in the 'app' folder
    from app import create_app

    #Start/Create the app with a selected Configuaration, if no config is defined in the environment variables the config 'default is used. The configurations are defined in the config.py file.
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')

config.py:
    #Import Operating System 
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

        @staticmethod
        def init_app(app):
            pass

    class DevelopmentConfig(Config):
        DEBUG = True

    class TestingConfig(Config):
        TESTING = True


    class ProductionConfig(Config):
        pass

    config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}