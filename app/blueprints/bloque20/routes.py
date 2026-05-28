from flask import Blueprint, render_template

bloque20_bp = Blueprint("bloque20", __name__, template_folder="templates")

@bloque20_bp.route("/")
def home():
    return render_template("bloque20.html")
