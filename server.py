from bottle import route, run, template


@route('/hello')
@route('/hello/<name>')
def index(name):
    return template('hello_world', name=name)


run(host='localhost', port=8080)
