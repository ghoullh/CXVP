from sanic import json, html, raw

from apis.browser import browser_bp
from browser.browser import CHROME
from browser.executor import Executor
from utils.util import get_logger

logger = get_logger(__name__)


@browser_bp.route("/execute", methods=['POST'])
async def browser_execute(request):
    data = request.json
    logger.debug(f"Execute Data: {data}")
    executor = Executor(data)
    await executor.run()
    return json({"message": "ok"})


@browser_bp.route("/script", methods=['POST'])
async def browser_script(request):
    data = request.json
    logger.debug(f"Script Data: {data}")
    executor = Executor(data)
    await executor.run()
    return json({"message": "ok"})


@browser_bp.route("/page/source", methods=['GET'])
async def browser_page_source(request):
    tab = request.args.get("tab", 0)
    return html(await CHROME.page_source(int(tab)))


@browser_bp.route("/page/screenshot", methods=['GET'])
async def browser_screenshot(request):
    tab = request.args.get("tab", 0)
    image_data = await CHROME.screenshot(int(tab))
    return raw(image_data, content_type="image/jpeg")
