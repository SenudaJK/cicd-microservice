from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Microservice</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #667eea;
                margin-bottom: 10px;
            }
            .status {
                color: #4CAF50;
                font-size: 24px;
                font-weight: bold;
                margin: 20px 0;
            }
            .info {
                background: #f5f5f5;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: left;
            }
            .info-item {
                margin: 10px 0;
                color: #333;
            }
            .links {
                margin-top: 30px;
            }
            .links a {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
            }
            .links a:hover {
                background: #5568d3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Pipeline Microservice</h1>
            <div class="status">✅ Status: Running Successfully!</div>
            <div class="info">
                <div class="info-item"><strong>Service:</strong> Flask Microservice</div>
                <div class="info-item"><strong>Time:</strong> {}</div>
                <div class="info-item"><strong>Environment:</strong> Kubernetes</div>
                <div class="info-item"><strong>Version:</strong> 1.0.0</div>
            </div>
            <div class="links">
                <a href="/health">Health Check</a>
                <a href="/info">System Info</a>
            </div>
        </div>
    </body>
    </html>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return html_content

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "cicd-microservice"
    }

@app.route("/info")
def info():
    return {
        "service": "CI/CD Microservice",
        "version": "1.0.0",
        "framework": "Flask",
        "python_version": os.sys.version,
        "hostname": os.environ.get("HOSTNAME", "unknown"),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
