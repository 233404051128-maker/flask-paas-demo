from flask import Flask
import datetime, platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html><head><meta charset="utf-8"><title>Flask PaaS Demo</title>
    <style>
    body {{ font-family: Arial; max-width: 640px; margin: 60px auto; }}
    .box {{ background:#DEEAF1; border-left: 5px solid #1F4E79; padding: 24px; border-radius: 8px; }}
    h1 {{ color: #1F4E79; }}
    </style></head><body>
    <h1>Ung dung Flask tren PaaS</h1>
    <div class="box">
    <p><b>Sinh vien:</b> NGO TRAN YEN VI – 233404051128</p>
    <p><b>Mon hoc:</b> Dien toan Dam may</p>
    <p><b>Mo hinh:</b> PaaS – Platform as a Service</p>
    <p><b>Python:</b> {platform.python_version()}</p>
    <p><b>Thoi gian server:</b> {datetime.datetime.now()}</p>
    </div>
    <p>Developer chi viet code – PaaS lo build, deploy, HTTPS, scaling!</p>
    </body></html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)