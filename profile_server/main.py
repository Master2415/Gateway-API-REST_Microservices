import logging
from flask import Flask, request, jsonify
import asyncio
import nats
from handlers.apiFunctions_handler import *
from handlers.healthFunctions_handler import *

START_TIME = time.time()
logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/profile/add', methods=['POST'])
def add_profile_router():
    return asyncio.run(AddProfile_handler())

@app.route('/profile/update', methods=['PUT'])
def update_profile_router():
    return asyncio.run(UpdateProfile_handler())

@app.route('/profile/delete/<email>', methods=['DELETE'])
def delete_profile_router(email):
    return asyncio.run(DeleteProfile_handler(email))

@app.route('/profile/search/<email>', methods=['GET'])
def get_profile_router(email):
    return asyncio.run(GetProfile_handler(email))

@app.route('/profile/getall', methods=['GET'])
def get_all_profiles_router():
    return asyncio.run(GetAllProfiles_handler())

@app.route('/profile/health', methods=['GET'])
def health_router():
    health_data = asyncio.run(health_handler(START_TIME))
    return jsonify(health_data.to_dict())

if __name__ == '__main__':
    app.run(port=8083)
