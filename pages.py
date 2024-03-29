import os, errno, re
from time import gmtime, strftime

from flask import Flask, render_template, abort, send_from_directory,make_response,send_file
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def pages(page=None):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
