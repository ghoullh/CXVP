import os

import psutil
from jinja2 import Environment, FileSystemLoader
from sanic import Sanic, json, html

from apis.browser import browser_bp
env = Environment(loader=FileSystemLoader("templates"))

app = Sanic("CXVP")

app.static("/static", "./static")

app.blueprint(browser_bp)


@app.route("/vnc")
async def vnc(request):
    vnc_password = os.environ.get('VNC_PASSWORD')
    template = env.get_template("vnc_lite.html")
    return html(template.render(VNC_PASSWORD=vnc_password))


@app.route('/healthCheck', methods=['GET'])
async def health_check(request):
    total = sum(p.memory_info().rss for p in psutil.process_iter()) / (1024 * 1024)
    return json({"memory": total})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, workers=1, auto_reload=False, single_process=True)
