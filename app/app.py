from flask import Flask, jsonify
import os
import socket
import platform
import time

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def dashboard():
    uptime = int(time.time() - START_TIME)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Self-Healing DevOps Platform</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 40px;
            }}

            .container {{
                max-width: 900px;
                margin: auto;
            }}

            .card {{
                background: white;
                padding: 25px;
                margin: 15px 0;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}

            .healthy {{
                color: green;
                font-weight: bold;
            }}

            .value {{
                font-size: 18px;
                margin: 8px 0;
            }}
        </style>
    </head>

    <body>

    <div class="container">

        <h1>Self-Healing DevOps Platform</h1>

        <div class="card">
            <h2>Application Health</h2>
            <p class="healthy">● HEALTHY</p>
            <p class="value">Service: Running</p>
        </div>

        <div class="card">
            <h2>Server Information</h2>
            <p class="value">Hostname: {socket.gethostname()}</p>
            <p class="value">Operating System: {platform.system()}</p>
            <p class="value">Platform: {platform.platform()}</p>
            <p class="value">Uptime: {uptime} seconds</p>
        </div>

        <div class="card">
            <h2>DevOps Environment</h2>
            <p class="value">Environment: {os.getenv("ENVIRONMENT", "local")}</p>
            <p class="value">Application Version: {os.getenv("APP_VERSION", "1.0")}</p>
        </div>

        <div class="card">
            <h2>Monitoring Endpoints</h2>
            <p class="value">Health Check: /health</p>
            <p class="value">System Status: /status</p>
        </div>

    </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "self-healing-devops-platform"
    })


@app.route("/status")
def status():
    return jsonify({
        "application": "running",
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "environment": os.getenv("ENVIRONMENT", "local"),
        "version": os.getenv("APP_VERSION", "1.0")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)