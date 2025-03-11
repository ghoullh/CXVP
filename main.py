import psutil
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/healthCheck', methods=['GET'])
def health_check():
    total = sum(p.memory_info().rss for p in psutil.process_iter()) / (1024 * 1024)
    return jsonify({"memory":total})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
