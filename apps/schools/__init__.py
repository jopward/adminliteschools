from flask import Blueprint

school_bp = Blueprint(
    "schools",
    __name__,
    template_folder="templates",
    static_folder="static"
)

from . import routes
