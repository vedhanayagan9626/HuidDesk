from flask import Blueprint, render_template
auth_bp = Blueprint("auth",__name__,static_folder = "static", template_folder= "templates")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return "<h1>Login pages</h1>"