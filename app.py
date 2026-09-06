import os
import datetime
import platform
from flask import Flask

app = Flask(__name__)

visit_count = 0  # Biến đếm lưu trong RAM của container

@app.route("/api/counter")
def counter():
    global visit_count
    visit_count += 1
    return {
        "so_lan_truy_cap": visit_count,
        "ghi_chu": "So nay se MAT khi container khoi dong lai!"
    }

@app.route("/api/info")
def info():
    ten_sinh_vien = os.environ.get("STUDENT_NAME", "NGO TRAN YEN VI")
    return {
        "sinh_vien": ten_sinh_vien,
        "nguon_du_lieu": "Environment Variable tren Render, KHONG hardcode trong code"
    }

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
    <p><b>Sinh vien:</b> NGO TRAN YEN VI 233404051128</p>
    <p><b>Mon hoc:</b> Dien toan Dam may</p>
    <p><b>Mo hinh:</b> PaaS – Platform as a Service</p>
    <p><b>Python:</b> {platform.python_version()}</p>
    <p><b>Thoi gian server:</b> {datetime.datetime.now()}</p>
    </div>
    <p>Developer chi viet code – PaaS lo build, deploy, HTTPS, scaling!</p>
    </body></html>
    """