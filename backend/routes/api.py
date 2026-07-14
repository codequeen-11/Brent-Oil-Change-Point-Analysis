from flask import Blueprint, jsonify

from services.analysis_service import (
    get_prices,
    get_events,
    get_dashboard_summary,
    get_change_point,
)

api = Blueprint(
    "api",
    __name__,
    url_prefix="/api",
)


@api.route("/prices")
def prices():

    return jsonify(get_prices())


@api.route("/events")
def events():

    return jsonify(get_events())


@api.route("/summary")
def summary():

    return jsonify(get_dashboard_summary())


@api.route("/change-point")
def change_point():

    return jsonify(get_change_point())