from flask import Blueprint

#Create a new blueprint
example = Blueprint('example', __name__)

#Import all bluebrint specific views and errors
from . import views, errors


