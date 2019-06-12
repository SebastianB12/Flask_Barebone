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
  - __init__.py
 - config.py
 - run.py
