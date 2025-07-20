from flask import Flask , Blueprint, render_template

QC_bp = Blueprint("QC", __name__, static_folder="static", template_folder="templates")

@QC_bp.route("/QC", methods=["GET", "POST"])
def QC():
    return "<h1> QC Stage </h1>"