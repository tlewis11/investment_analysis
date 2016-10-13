from bottle import route, run, template

@route('/dividends')
def index():
    name = 'dividends' 
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

