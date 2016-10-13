import json

from bottle import route, run, template

@route('/dividends')
def index():
    name = 'dividends' 
    endpoints = ['getYield']

    response_json = json.dumps(endpoints)
    return response_json

run(host='localhost', port=8080, debug=True)

