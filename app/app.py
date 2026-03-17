import os
import socket
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_vault_token():
    vault_addr = os.getenv('VAULT_ADDR', 'http://localhost:8200')
    role_id = os.getenv('VAULT_ROLE_ID')
    secret_id = os.getenv('VAULT_SECRET_ID')

    if not role_id or not secret_id:
        return None, None

    response = requests.post(
        f"{vault_addr}/v1/auth/approle/login",
        json={"role_id": role_id, "secret_id": secret_id},
        timeout=5
    )

    if response.status_code == 200:
        token = response.json()["auth"]["client_token"]
        return vault_addr, token
    return None, None

def get_db_secrets():
    vault_addr, token = get_vault_token()
    if not token:
        return {"status": "vault not configured"}

    response = requests.get(
        f"{vault_addr}/v1/prodstack/data/db",
        headers={"X-Vault-Token": token},
        timeout=5
    )

    if response.status_code == 200:
        data = response.json()["data"]["data"]
        return {
            "host": data.get("host"),
            "port": data.get("port"),
            "username": data.get("username"),
            "password_length": len(data.get("password", "")),
            "password": "***HIDDEN***"
        }
    return {"status": "failed to fetch secrets"}

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'hostname': socket.gethostname()
    }), 200

@app.route('/data')
def data():
    return jsonify({
        'message': 'Hello from ProdStack',
        'hostname': socket.gethostname(),
        'version': os.getenv('APP_VERSION', '2.0.0')
    }), 200

@app.route('/secrets-test')
def secrets_test():
    db = get_db_secrets()
    return jsonify({
        'hostname': socket.gethostname(),
        'vault_connected': 'host' in db,
        'db_secrets': db
    }), 200

@app.route('/')
def index():
    return jsonify({
        'app': 'ProdStack',
        'hostname': socket.gethostname()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
