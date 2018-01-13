#!/usr/bin/env python

from bottle import Bottle, run, route, static_file, view, template, post, request, debug
# from bottle import route, run, template, static_file

import os, sys
import turret

dirname = os.path.dirname(sys.argv[0])

app = Bottle()
debug(True)


@app.route('/')
def index():
	return template('dashboard', get_url=app.get_url, title='Turret Control - Dashboard')


@app.route('/ajax/turret/fire', method="POST")
def fire_turret(): #3733
    speed = request.forms.get('speed')
    shots = request.forms.get('shots')

    turret.flywheelAction(speed, shots)
    return '{"speed":"'+str(speed)+'", "shots":"'+str(shots)+'"}'


@app.route('/assets/css/<filename:re:.*\.css>', name='styles')
def send_css(filename):
	return static_file(filename, root='./assets/css')

@app.route('/assets/js/<filename:re:.*\.js>', name='scripts')
def send_css(filename):
	return static_file(filename, root='./assets/js')


run(app, host='0.0.0.0', port = 8080)