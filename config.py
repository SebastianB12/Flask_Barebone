#See the flask documentation (http://flask.pocoo.org/docs/1.0/config/)\
# for the general purpose of a configuration

#Import operating system functionalities
import os
#Define the Base Directory, which is the path there this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

#Definition of the Configuration class, if you are not familiar with classes please\
#check out the documentation (https://docs.python.org/3/tutorial/classes.html ) \
#or these tutorials (https://www.w3schools.com/python/python_classes.asp,\
#https://www.w3schools.com/python/python_inheritance.asp)

#Define the Config Class
class Config:
    #To use user sessions in Flask you need to set a secret key.

    #!!!!!Please change the string or set the environment variable!!!!!!
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    #Define a for now empty init_app() class method, that take the
    #application instance as an argument. It can be used for more\
    #complex initialization procedures
    #(A staticmehod (@staticmethod) is a method of a class,\
    # which makes sense to be present in the class, but can not change class state)
    @staticmethod
    def init_app(app):
        pass

#Several Configuation Classes which inherit from the Config Base Class:

class DevelopmentConfig(Config):
    #Enable the FLASK Debug Mode (Automatic Application Reload after every
    #change and interactive debugger in the browser)
    DEBUG = True

class TestingConfig(Config):
    #Enable the FLASK Testing Mode (Exceptions are propagated and not
    #handled by the the app’s error handlers)
    TESTING = True


class ProductionConfig(Config):
    #Nothing special for production mode
    pass

#Dictionary to easily access the different configurations:
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
