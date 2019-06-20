# Flask Barebone

Flask Barebone is a minimal Flask Setup, which can be easily used for starting off every Flask project.
The setup includes:
- A typical Flask folder structure, which is easy to expand
- Two prepared blueprints
- Prepared Configuration file for more complex application configuration
- Bootstrap 4 in the a base template

The structure is the following:

Projectfolder:
- app
  - main (main blueprint)
  - exmample (2nd blueprint)
  - static (static files)
  - templates
    - example (templates for 2nd blueprint)
    - base.html (base template with Boostrap 4)
    - index.html (sample template for the main blueprint)
  - \__init\__.py
 - config.py
 - run.py

To quickly deploy the flask app you can use e.g. Pythonanyshwere (https://www.pythonanywhere.com).
Just get your free account and create a web app.
In the folder of the web app, open the bash console and pull the data from the repository.(git clone https://github.com/SebastianB12/Flask_Barebone:foldername .).
Change the path and the name of the application in the WSGI file:

```python
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys

# add your project directory to the sys.path
project_home = u'/home/SebastianB12/mysite/Flask_Barebone'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from run import app as application  # noqa
```
