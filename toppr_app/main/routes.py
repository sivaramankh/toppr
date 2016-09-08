from flask import render_template, redirect
from . import main


@main.route('/')
def index():
    return redirect('/list')


@main.route('/list')
def get_list():
    return render_template("list.html")


@main.route('/list/number')
def get_list_by_number():
    return render_template("list_number.html")


@main.route('/search')
def search_record():
    return render_template("search.html")


@main.route('/stats/main')
def get_stats():
    return render_template("stats.html")
