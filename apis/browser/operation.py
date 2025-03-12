from sanic import json

from apis.browser import browser_bp
from browser.browser import CHROME
from utils.util import get_logger

logger = get_logger(__name__)


@browser_bp.route("/execute", methods=['POST'])
async def browser_execute(request):
    data = request.json
    logger.debug(data)
    await CHROME.execute(data['type'], data['value'])
    return json({"message": "ok"})
