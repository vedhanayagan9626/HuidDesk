from flask import Flask , Blueprint, render_template

weighing_bp = Blueprint("weighing", __name__, static_folder="static", template_folder="templates")

@weighing_bp.route("/weighing", methods=["GET", "POST"])
def weighing():
    return "<h1> Weighing Stage </h1>"
