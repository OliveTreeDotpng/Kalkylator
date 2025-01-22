from flask import Blueprint, render_template

# Förklarar vad Blueprint är och varför det används. Beskriver rutten och dess koppling till HTML-sidan.
bp = Blueprint("name", __name__)

@bp.route("/")
def startpage():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def logiin():
    if request.method == "POST"

    # Sida 18 upf-5-calcing.marp.pdf