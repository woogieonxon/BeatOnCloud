"""_summary_

    Returns:
        _type_: _description_
"""
from flask import Blueprint, render_template


bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("index.html")
