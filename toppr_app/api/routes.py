from flask import url_for, request, jsonify
from . import api
from .helpers import query_db, parse_params, stats


@api.route('/list', methods=["GET"])
def get_list():
    """Endpoint for getting the whole list"""

    result = query_db.query({})

    return jsonify(result)


@api.route('/list/<int:battle_no>', methods=["GET"])
def get_battle_by_no(battle_no):
    """Endpoint for getting record by battle number"""

    parameters = {"battle_number" : [battle_no] }
    result = query_db.query(parameters)

    if result == []:
        result = {"Error" : "Your query didnt match any records."}

    print(result)

    return jsonify(result)


@api.route('/count', methods=["GET"])
def get_count():
    """Endpoint for getting the number of records"""

    result = query_db.query({})

    return jsonify({"count" : len(result)})


@api.route('/search', methods=["GET"])
def search_list():
    """Endpoint for searching the records"""

    req_parameters = request.args
    parameters = parse_params.parser(req_parameters)
    result = query_db.query(parameters)

    if result == []:
        result = {"Error" : "Your query didnt match any records."}


    return jsonify(result)


@api.route('/stats', methods=['GET'])
def battle_stats():
    """Endpoint for getting the stats of the dataset"""

    result = query_db.query({})
    bat_stats = stats.main_stats(result)

    return jsonify({"battle_stats" : bat_stats})


@api.route('/stats/active', methods=['GET'])
def most_active_stats():
    """Endpoint for getting the most active stats of the dataset"""

    result = query_db.query({})
    most_active = stats.most_active_fn(result)

    return jsonify({"most_active" : most_active})


@api.route('/stats/largest', methods=['GET'])
def largest_army_stats():
    """Endpoint for getting the largest army stats of the dataset"""

    result = query_db.query({})
    largest_army = stats.largest_army(result)

    return jsonify({"largest_army" : largest_army})


@api.route('/stats/year', methods=['GET'])
def battle_stats_year():
    """Endpoint for getting the yearwise battle stats of the dataset"""

    result = query_db.query({})
    year_stats = stats.year(result)

    return jsonify(year_stats)
