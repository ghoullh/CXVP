from sanic import Blueprint

browser_bp = Blueprint("browser", url_prefix="/browser")

from . import operation