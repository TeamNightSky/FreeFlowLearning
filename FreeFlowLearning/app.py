import jinja2
import os

from flask import (
    Flask, 
    render_template,
    request
)

NAME = os.path.split(os.getcwd())[-1]

RESOURCE_DIRS = [
    f'{NAME}/Frontend/templates/',
    f'{NAME}/Frontend/static/',
    f'{NAME}/Docs/'
]

app = Flask(__name__)

template_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(RESOURCE_DIRS)
])
app.jinja_loader = template_loader


@app.route('/')
def index():
    return render_template('index.html')

