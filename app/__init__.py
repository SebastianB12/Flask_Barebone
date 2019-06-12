##Application Package Constructor##

#Import the core Flask Package
from flask import Flask
#Import our defined Configuration
from config import config

#This the Application Factory Function, it is invoked\
#by the start file "run.py" with the config_name as a parameter
def create_app(config_name):

    #Initialize the FLASK App
    #__name__ returns from where the function is invoked:
    #This is needed so that Flask knows where to look for
    #templates, static files, and so on
    app = Flask(__name__)
    #Select the Configuration out of the configuration dictionary
    # in the config.py file
    app.config.from_object(config[config_name])
    #Invoke the init_app() method to do some more complex\
    #initialization, if needed
    config[config_name].init_app(app)

    #Register Blueprints
    #Blueprints are like mini application inside the bigger application
    #with routes, error handlers, templates and so on. They are used
    #to get a more structured application. Here the "main" blueprint is
    #registered. All the blueprint's files are in the "main" folder,
    # the templates are in the template folder
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #For Clarification I created a second blueprint called "example"
    from .example import example as example_blueprint
    app.register_blueprint(example_blueprint, url_prefix='/example')
    return app
