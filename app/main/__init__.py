from flask import Blueprint

#Create a new blueprint
main = Blueprint('main', __name__)

#Import all bluebrint specific views and errors
from . import views, errors


