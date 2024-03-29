"""Flask routing.

Specifying routes for our Flask app is simple. We do it just by providing
the desired route in the `@app.route()` decorator. Sometimes our routes have
dynamic parameters. For example:
* `/posts/23` -> The number 23 (post id) is dynamic
* `/repo/flask-introduction/stars` -> The name of the repo (flask-introduction)
                                      is dynamic

Supporting dynamic routing parameters is really simple. We just need to
specify the desired dynamic portion by giving it a name and surrounding
it between `<>`.
"""
import json
from flask import Flask, render_template, abort

app = Flask(__name__)

AUTHORS_INFO = [
    {
        'last_name': 'Poe',
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Edgar_Allan_Poe_2_retouched_and_transparent_bg.png'
    },
    {
        'last_name': 'Borges',
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Jorge_Luis_Borges_1951%2C_by_Grete_Stern.jpg'
    }
]


@app.route('/')
def authors():
    return render_template('routing/authors.html', len = len(AUTHORS_INFO), Authors = AUTHORS_INFO)


@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    author_finded = find_author(authors_last_name)
    if author_finded != False:
        return render_template('routing/author.html', author=author_finded)
    else:
        abort(404)

def find_author(authors_last_name):
    for author in AUTHORS_INFO:
        if author['last_name'] == authors_last_name:
            return author
        else:
            return False


@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404            