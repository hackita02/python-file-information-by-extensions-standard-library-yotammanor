from bottle import route, run, template
import os
import pathlib

PORT = int(os.environ.get("PORT", 5000))
BASE_PATH = pathlib.Path(__file__).parent

@route('/hello')
@route('/hello/<name>')
def index(name):
    return template('hello_world', name=name)


run(host='0.0.0.0', port=PORT)
