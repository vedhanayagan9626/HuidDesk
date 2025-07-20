from flask import Blueprint, render_template

main_bp = Blueprint("main",__name__, static_folder="static", template_folder="templates")

@main_bp.routes('/mainpage', methods=['GET', 'POST'])
def main():
    return render_template('/dashboard')