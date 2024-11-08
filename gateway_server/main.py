from flask import Flask, request, jsonify
import asyncio
import nats
import logging
from handlers.userFunctions_handler import *
from handlers.healthFunctions_handler import *

START_TIME = time.time()
logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def user_login_router():
    return asyncio.run(userLogin_handler())

@app.route('/api/user', methods=['POST'])
def user_add_router():
    return asyncio.run(userAdd_handler())

@app.route('/api/user', methods=['PUT'])
def user_update_router():
    return asyncio.run(userUpdate_handler())

@app.route('/api/user/<email>', methods=['GET'])
def user_get_by_email_router(email):
    return asyncio.run(userGet_handler(email))

@app.route('/api/user/<email>', methods=['DELETE'])
def user_delete_router(email):
    return asyncio.run(userDelete_handler(email))

@app.route('/api/health', methods=['GET'])
def health_router():
    health_data = asyncio.run(health_handler(START_TIME))
    return jsonify(health_data.to_dict())

if __name__ == '__main__':
    app.run(port=8084)
