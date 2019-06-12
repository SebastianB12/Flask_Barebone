#Import operating system functionalities
import os 
#import the create_app function from our __init__.py file in the 'app' folder
from app import create_app

#Start/Create the app with a selected Configuaration, if no config is defined in the \
#environment variables the config 'default is used. The configurations are defined in the\
# config.py file.
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
