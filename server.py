from bottle import route, run, template, redirect, view
import os
import pathlib
import calendar
import datetime

PORT = int(os.environ.get("PORT", 5000))
BASE_PATH = pathlib.Path(__file__).parent


@route('/hello/')
@route('/hello/<name>/')
def index(name='world'):
    return template('hello_world', name=name)


@route('<path:re:.+[^/]$>')
def add_slash(path):
    return redirect(path + "/")


@route('/')
@route('/<year>/')
@route('/<year>/<month>/')
@view('calendar')
def month_view(year=None, month=None):
    year_param = year or datetime.datetime.now().year
    month_param = month or datetime.datetime.now().month
    prev = '/{}/{}'.format(year_param, int(month_param) - 1)
    next_month = '/{}/{}'.format(year_param, int(month_param) + 1)
    return dict(cal=calendar.HTMLCalendar().formatmonth(int(year_param), int(month_param)), prev=prev,
                next=next_month)


run(host='0.0.0.0', port=PORT)
