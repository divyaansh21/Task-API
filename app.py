from flask import Flask, render_template, request, redirect, url_for
import logging as logger

logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

# Mock Database - Pre-filled with some dummy data for the demo
servers = [
    {"id": 1, "name": "AWS-Prod-DB", "ip": "10.0.1.5", "status": "Running"},
    {"id": 2, "name": "Jenkins-Master", "ip": "192.168.1.50", "status": "Running"},
    {"id": 3, "name": "Legacy-Worker", "ip": "10.0.2.12", "status": "Stopped"}
]

@flaskAppInstance.route('/')
def home():
    return render_template('index.html', servers=servers)

@flaskAppInstance.route('/add', methods=['POST'])
def add_server():
    name = request.form.get('name')
    ip = request.form.get('ip')
    status = request.form.get('status')
    
    if name and ip:
        new_server = {
            "id": len(servers) + 1,
            "name": name,
            "ip": ip,
            "status": status
        }
        servers.append(new_server)
    return redirect(url_for('home'))

@flaskAppInstance.route('/delete/<int:id>')
def delete_server(id):
    global servers
    servers = [s for s in servers if s['id'] != id]
    return redirect(url_for('home'))

if __name__ == "__main__":
    # Host 0.0.0.0 is required for Docker containers
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=False)
