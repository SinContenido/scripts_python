from bottle import route, run, template

@route('/hola/<name>')
def hola(name):
    return template('<b>Hola {{name}}</b>!', name=name)

"""@route('/')
def index(name):
    return template('<b>Hola world</b>!',name=name)"""
    
@route('/hola/<name>')
def hola(name):
    return template('<b>Hola {{name}}</b>!', name=name)

run(host='localhost', port=8080)