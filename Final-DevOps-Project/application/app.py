import hashlib
import hmac
import logging
import math
import os
import socket
import time
from flask import Flask, jsonify, render_template_string, request
from prometheus_client import Counter, Histogram, CONTENT_TYPE_LATEST, generate_latest

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
requests_total = Counter("notes_requests_total", "HTTP requests", ["path", "status"])
request_seconds = Histogram("notes_request_seconds", "Request duration", ["path"])
page = """<!doctype html>
<html><head><title>DevOps Notes</title>
<style>body{font-family:system-ui;max-width:680px;margin:50px auto;padding:20px;background:#f5f5f5;color:#222}main{background:white;padding:28px;border:1px solid #ddd;border-radius:8px}code{background:#eee;padding:3px}li{margin:10px 0}</style>
</head><body><main><h1>{{ greeting }}</h1><p>A small application for my DevOps exercises.</p>
<ul><li>Version: <strong>{{ version }}</strong></li><li>Environment: {{ environment }}</li><li>Pod: <code>{{ hostname }}</code></li></ul>
<p><a href="/health">Health</a> · <a href="/api/status">Application status</a> · <a href="/metrics">Metrics</a></p>
<p>Calculator: POST numbers and an operation to <code>/api/calculate</code>.</p></main></body></html>"""


def calculate(a, b, operation):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    else:
        raise ValueError("Unknown operation")
    if not math.isfinite(result):
        raise ValueError("Result is too large")
    return result


@app.before_request
def start_timer():
    request.started = time.monotonic()


@app.after_request
def record_request(response):
    path = request.url_rule.rule if request.url_rule else "unknown"
    if path != "/metrics":
        requests_total.labels(path, str(response.status_code)).inc()
        request_seconds.labels(path).observe(time.monotonic() - request.started)
        app.logger.info("method=%s path=%s status=%s", request.method, path, response.status_code)
    return response


@app.get("/")
def home():
    return render_template_string(page, greeting=os.getenv("GREETING", "DevOps Notes"),
                                  version=os.getenv("APP_VERSION", "1.0"),
                                  environment=os.getenv("ENVIRONMENT", "development"),
                                  hostname=socket.gethostname())


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/ready")
def ready():
    if not os.getenv("API_TOKEN"):
        return jsonify(status="configuration missing"), 503
    return jsonify(status="ready")


@app.get("/api/status")
def status():
    return jsonify(version=os.getenv("APP_VERSION", "1.0"), hostname=socket.gethostname(),
                   environment=os.getenv("ENVIRONMENT", "development"))


@app.post("/api/calculate")
def calculator():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or any(key not in data for key in ("a", "b", "operation")):
        return jsonify(error="Provide a, b and operation"), 400
    try:
        if any(type(data[key]) not in (int, float) or not math.isfinite(data[key]) for key in ("a", "b")):
            return jsonify(error="Use finite numbers"), 400
        return jsonify(result=calculate(data["a"], data["b"], data["operation"]))
    except (ValueError, OverflowError) as error:
        return jsonify(error=str(error)), 400


@app.get("/api/private")
def private():
    token = os.getenv("API_TOKEN", "")
    supplied = request.headers.get("X-API-Token", "")
    if not token or not hmac.compare_digest(supplied.encode(), token.encode()):
        return jsonify(error="Unauthorized"), 401
    return jsonify(message="Secret authentication worked")


@app.get("/work")
def work():
    hashlib.pbkdf2_hmac("sha256", b"load-exercise", b"devops", 200000)
    return jsonify(status="done")


@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
