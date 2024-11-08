import http
from communication.communication import sendLog
from handlers.routes import *
from models.Log import Log
import datetime
import httpx
from flask import request, jsonify

async def userLogin_handler():
    try:
        data = request.data

        async with httpx.AsyncClient() as client:
            response = await client.post(URL_LOGIN, data=data)

        log = Log(
            app_name = "API-GATEWAY",
            log_type = "INFO",
            module = "USER-LOGIN-GATEWAY",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Request redirected successfully",
            description = "A login request was successfully redirected" 
        )
        await sendLog(log)            
        return response.text, response.status_code

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        return 'error: ' + error_message, http.HTTPStatus.INTERNAL_SERVER_ERROR

async def userAdd_handler():
    try:
        data = request.data

        async with httpx.AsyncClient() as client:
            response = await client.post(URL_USER_ADD, data=data)

        log = Log(
            app_name = "API-GATEWAY",
            log_type = "INFO",
            module = "USER-ADD-GATEWAY",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Request redirected successfully",
            description = "A login request was successfully redirected" 
        )
        await sendLog(log)            
        return response.text, response.status_code

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        return 'error: ' + error_message, http.HTTPStatus.INTERNAL_SERVER_ERROR

async def userUpdate_handler():
    try:
        data = request.get_json()
        token = request.headers.get('Authorization')
        headers = {'Authorization': token}

        async with httpx.AsyncClient() as client:
            response = await client.put(URL_USER_UPDATE, json=data, headers=headers)

        log = Log(
            app_name="API-GATEWAY",
            log_type="INFO",
            module="USER-UPDATE-GATEWAY",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Request redirected successfully",
            description="A user update request was successfully redirected"
        )
        await sendLog(log)

        return response.text, response.status_code

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        return 'error: ' + error_message, http.HTTPStatus.INTERNAL_SERVER_ERROR

async def userDelete_handler(email):
    try:
        token = request.headers.get('Authorization')
        headers = {'Authorization': token}

        async with httpx.AsyncClient() as client:
            response = await client.delete(URL_USER_DELETE + email, headers=headers)

        log = Log(
            app_name="API-GATEWAY",
            log_type="INFO",
            module="USER-DELETE-GATEWAY",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Request redirected successfully",
            description="A user delete request was successfully redirected"
        )
        await sendLog(log)

        return response.text, response.status_code

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        return 'error: ' + error_message, http.HTTPStatus.INTERNAL_SERVER_ERROR
    
async def userGet_handler(email):
    try:
        token = request.headers.get('Authorization')
        headers = {'Authorization': token}

        async with httpx.AsyncClient() as client:
            user_response = await client.get(URL_USER_GET + email, headers=headers)
            profile_response = await client.get(URL_PROFILE_GET + email, headers=headers)

        final_response = {
            'user': {},
            'profile': {}
        }

        if user_response.status_code == 200:
            final_response['user'] = user_response.json()
        else:
            final_response['user'] = {
                'error': f"Unable to retrieve user information. Status: {user_response.status_code}",
                'response': user_response.text
            }

        if profile_response.status_code == 200:
            final_response['profile'] = profile_response.json()
        else:
            final_response['profile'] = {
                'error': f"Unable to retrieve profile information. Status: {profile_response.status_code}",
                'response': profile_response.text
            }

        log = Log(
            app_name="API-GATEWAY",
            log_type="INFO",
            module="USER-GET-GATEWAY",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Request redirected successfully",
            description="A user get request was successfully redirected"
        )
        await sendLog(log)

        if user_response.status_code == 200 and profile_response.status_code == 200:
            return final_response, http.HTTPStatus.OK
        else:
            return final_response, http.HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        return {'error': error_message}, http.HTTPStatus.INTERNAL_SERVER_ERROR



