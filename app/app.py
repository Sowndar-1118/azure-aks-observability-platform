from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
import socket
import datetime
import platform

app = Flask(__name__)

# Prometheus Counter
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()

    return jsonify({
        "project": "Azure AKS Observability Platform",
        "message": "Application is running successfully",
        "hostname": socket.gethostname(),
        "timestamp": str(datetime.datetime.utcnow())
    })


@app.route("/health")
def health():
    REQUEST_COUNT.inc()

    return jsonify({
        "status": "healthy"
    })


@app.route("/info")
def info():
    REQUEST_COUNT.inc()

    return jsonify({
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "architecture": platform.machine(),
        "timestamp": str(datetime.datetime.utcnow())
    })


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": "text/plain"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
