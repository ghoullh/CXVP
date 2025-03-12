import psutil
from sanic import Sanic, json

from apis.browser import browser_bp

app = Sanic("SVXP")

app.blueprint(browser_bp)


@app.route('/healthCheck', methods=['GET'])
async def health_check(request):
    total = sum(p.memory_info().rss for p in psutil.process_iter()) / (1024 * 1024)
    return json({"memory": total})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, workers=1, auto_reload=False, single_process=True)
