from flask import render_template, redirect, url_for, abort, flash
from . import example

@example.route('/example_page')
def example_page():
    return render_template('example/example_page.html')